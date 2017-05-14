from collections import deque
from joblib import Parallel, delayed
from utils import getWord, isWordInArr, definitions
from operator import itemgetter
from multiprocessing import Pool, cpu_count

class BKTree:
    def __init__(self, distance_func):
        self._tree = None
        self._distance_func = distance_func
        self.radius = definitions['BKTreeRadius']

    def add(self, node):
        if self._tree is None:
            self._tree = (node, {})
            return

        current, children = self._tree
        while True:
            dist = self._distance_func(node, current)
            target = children.get(dist)
            if target is None:
                children[dist] = (node, {})
                break
            current, children = target

    def parallelAdd(self, dictionaryArray):
        Parallel()(delayed(BKTree.add)(self, getWord(word)) for word in dictionaryArray)

    def search(self, node):
        if self._tree is None:
            return []

        candidates = deque([self._tree])
        result = []
        while candidates:
            candidate, children = candidates.popleft()
            dist = self._distance_func(node.lower(), candidate)
            if dist <= self.radius:
                result.append((dist, candidate))

            low, high = dist - self.radius, dist + self.radius
            candidates.extend(c for d, c in children.items()
                              if low <= d <= high)

        result.sort(key=itemgetter(0))
        return result[:10]

    def findMistakes(self, args):
        word, book = args
        results = self.search(word)
        if not isWordInArr(results, word):
            indexes = [i for i, x in enumerate(book) if x == word]
            return word, (indexes, results)