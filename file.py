import re

file = open(r"C:\Users\bengi\OneDrive\Documents\harry_potter.txt")
text = file.read()
file.close()

#Convert all text to lower case and remove special characters
text = text.lower() 
text = re.sub("\n", " ", text)
regex = re.compile('[^a-zA-Z \']')
text = regex.sub('', text)

wordList = text.split(' ')
wordDict = {}

#Count number of times each word appears, store it in dictionary
for word in wordList: 
    if word in wordDict.keys():
        wordDict[word] += 1
    else:
        wordDict[word] = 1

#Sort in order of word frequency, with most common words appearing first
wordDict = sorted(wordDict.items(), key=lambda x: x[1], reverse=True) 
print("Dictionary length = {}".format(len(wordDict)))

#Output dictionary to text file
with open(r'harry_potter_corpus.txt', 'w') as f: 
    print(wordDict, file=f)
