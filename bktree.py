from collections import deque
from joblib import Parallel, delayed
from utils import getWord, isWordInArr
from operator import itemgetter

spellingMistakes = {}

class BKTree:
    def __init__(self, distance_func):
        self._tree = None
        self._distance_func = distance_func

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

    def search(self, node, radius):
        if self._tree is None:
            return []

        candidates = deque([self._tree])
        result = []
        while candidates:
            candidate, children = candidates.popleft()
            dist = self._distance_func(node.lower(), candidate)
            if dist <= radius:
                result.append((dist, candidate))

            low, high = dist - radius, dist + radius
            candidates.extend(c for d, c in children.items()
                              if low <= d <= high)
        result.sort(key=itemgetter(0))
        return result[:10]

    def findMistakes(self, word, book):
        global spellingMistakes
        results = self.search(word, 5)
        if not isWordInArr(results, word):
            indexes = [i for i, x in enumerate(book) if x == word]
            spellingMistakes[word] = (indexes, results)