import re
import string
from pickle import dump, load, HIGHEST_PROTOCOL

definitions = {
    'ReadFilePath': 'book.txt',
    'DictionaryPath': 'Dictionary/dictionary.txt',
    'TreeSavePath': 'SaveFiles/bktree.save',
    'BookPathAndExt': 'Books/*.txt',
    'BKTreeRadius': 1,
    'LoadFromFile': True
}

def getWord(text):
    text = text.strip('\n')
    return re.compile(r"[a-zA-Z'`]*$").findall(text)[0]

def readFromFile(fileName, readLines):
    with open(fileName, encoding="utf8") as f:
        return f.readlines() if readLines else f.read()

def saveObjectToFile(object, savePath):
    with open(savePath, 'wb') as output:
        dump(object, output, HIGHEST_PROTOCOL)

def loadObjectFromFile(loadPath):
    with open(loadPath, 'rb') as input:
        return load(input)

def isWordInArr(arr, word):
    for elem in arr: return True if word.lower() == elem[1].lower() else False

def getBook(path):
    book = readFromFile(path, readLines=False)
    book = ''.join(ch if ch not in getPunctuation() else ' ' for ch in book)
    return [s for s in set(filter(None, ''.join([i for i in book if not i.isdigit()]).split(' '))) if len(s) > 1]

def getPunctuation():
    exclude = set(string.punctuation)
    exclude.add('\n')
    exclude.add('\r')
    exclude.add('-')
    exclude.add('—')
    exclude.add('“')
    exclude.add('”')
    exclude.add('’')
    return exclude