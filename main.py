import utils as u
import stringmetrics
import bktree
from glob import glob
from multiprocessing import Pool, cpu_count


def main():
    tree = None
    if not u.definitions['LoadFromFile']:
        dictionaryArray = u.readFromFile(u.definitions['DictionaryPath'], readLines=True)
        tree = bktree.BKTree(stringmetrics.levenshtein)
        tree.parallelAdd(dictionaryArray)
        u.saveObjectToFile(object=tree, savePath=u.definitions['TreeSavePath'])
    else:
        tree = u.loadObjectFromFile(u.definitions['TreeSavePath'])

    book = u.getBook(glob(u.definitions['BookPathAndExt'])[0])
    p = Pool(processes=cpu_count())
    spellingMistakes = p.map(tree.findMistakes, [(word, book) for word in book])
    spellingMistakes = [x for x in spellingMistakes if x is not None]
    print(spellingMistakes)


if __name__ == '__main__':
    try:
        main()
    except Exception as ex:
        print(ex)