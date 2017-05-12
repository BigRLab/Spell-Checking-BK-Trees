import re
from pickle import dump, load, HIGHEST_PROTOCOL

definitions = {
    'ReadFilePath': 'book.txt',
    'DictionaryPath': 'Dictionary/dictionary.txt',
    'TreeSavePath': 'SaveFiles/bktree.save',
    'BookPathAndExt': 'Books/*.txt'
}

def getWord(text):
    text = text.strip('\n')
    return re.compile(r"[a-zA-Z'`]*$").findall(text)[0]

def readFromFile(fileName, readLines):
    with open(fileName) as f:
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
    return readFromFile(path, readLines=False).replace('\n', ' ').replace('\r', '').replace('.', '').replace(',', '').replace(';', '').replace(':', '').split(' ')