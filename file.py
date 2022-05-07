import re
import json
import os

def readText(fileName):
    file = open(fileName, encoding="utf-8")
    text = file.read()
    file.close()
    return text

def readDict(fileName):
    with open(fileName, 'r', encoding='utf-8') as handle:
        wordDict = dict(json.load(handle))
    return wordDict

def formatText(text):
    text = re.sub("[，\-()Ｘ（）…！「。？一」．１２３４５６７８９－—：；a-zA-ZＴＰＣＨＭＬＤａＩＷＦＧ〇ｂ[\n\u3000 ]", "", text)
    return text

def updateDictionary(text, wordDict):
    wordList = text.split(' ')
    #Count number of times each word appears, store it in dictionary
    for word in text: 
        if word in wordDict.keys():
            wordDict[word] += 1
        else:
            wordDict[word] = 1
    print("Dictionary length = {}".format(len(wordDict)))
    return wordDict

def sortDictionary(wordDict):
    #Sort in order of word frequency, with most common words appearing first
    wordDict = sorted(wordDict.items(), key=lambda x: x[1], reverse=True)
    wordDict = dict(wordDict)
    return wordDict

#print("Dictionary length = {}".format(len(wordDict)))

def printToFile(wordDict, fileName):
    #Output dictionary to text file
    with open(fileName, 'w', encoding='utf-8') as handle:
        json.dump(wordDict, handle, ensure_ascii=False)

def createDict(outputFile):
    printToFile({}, outputFile)

def updateDict(fileName, outputFile):
    text = readText(fileName)
    text = formatText(text)
    wordDict = readDict(outputFile)
    wordDict = updateDictionary(text, wordDict)
    wordDict = sortDictionary(wordDict)
    printToFile(wordDict, outputFile)

def createCorpusFromDirectory(directory, corpus):
    createDict(corpus)
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.txt'):
                print("Reading from {}".format(file))
                updateDict(os.path.join(root, file), corpus)

createCorpusFromDirectory(r"C:\Users\bengi\Calibre Library", r"C:\Users\bengi\Calibre Library\corpus.json")
