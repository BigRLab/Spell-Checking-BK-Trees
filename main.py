import utils as u
import stringmetrics
import bktree
from glob import glob
from joblib import Parallel, delayed


def main(loadTreeFromFile):
    tree = None
    if not loadTreeFromFile:
        dictionaryArray = u.readFromFile(u.definitions['DictionaryPath'], readLines=True)
        tree = bktree.BKTree(stringmetrics.levenshtein)
        tree.parallelAdd(dictionaryArray)
        u.saveObjectToFile(object=tree, savePath=u.definitions['TreeSavePath'])
    else:
        tree = u.loadObjectFromFile(u.definitions['TreeSavePath'])

    book = u.getBook(glob(u.definitions['BookPathAndExt'])[0])
    for word in set(book):
        tree.findMistakes(word, book)
    print(bktree.spellingMistakes)


if __name__ == '__main__':
    try:
        main(loadTreeFromFile=True)
    except Exception as ex:
        print(ex)