import re

file = open(r"C:\Users\bengi\OneDrive\Documents\harry_potter.txt")
text = file.read()
file.close()

text = text.lower()
text = re.sub("\n", " ", text)
regex = re.compile('[^a-zA-Z \']')
text = regex.sub('', text)

wordList = text.split(' ')
wordDict = {}

for word in wordList:
    if word in wordDict.keys():
        wordDict[word] += 1
    else:
        wordDict[word] = 1

wordDict = sorted(wordDict.items(), key=lambda x: x[1], reverse=True)
print("Dictionary length = {}".format(len(wordDict)))

with open(r'harry_potter_corpus.txt', 'w') as f:
    print(wordDict, file=f)
