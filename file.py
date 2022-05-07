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
    for word in text: 
        if word in wordDict.keys():
            wordDict[word] += 1
        else:
            wordDict[word] = 1
    print("Text length = {}".format(len(text)))
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

def updateCorpus(fileName, wordDict):
    text = readText(fileName)
    text = formatText(text)
    wordDict = updateDictionary(text, wordDict)
    return wordDict

def createCorpusFromDirectory(directory, corpus):
    wordDict = {}
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.txt'):
                print("Reading from {}".format(file))
                wordDict = updateCorpus(os.path.join(root, file), wordDict)
    print("Sorting dictionary")
    wordDict = sortDictionary(wordDict)
    print("Storing dictionary in {}".format(corpus))
    printToFile(wordDict, corpus)

createCorpusFromDirectory(r"C:\Users\bengi\Calibre Library", r"C:\Users\bengi\Calibre Library\corpus.json")
