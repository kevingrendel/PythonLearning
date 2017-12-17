#read entire file
#use regex and match on alpha words
#create dictionary with key as the word, and value being object
    # word, 
    # length, 
    # count of occurances, 
    # list of index locations in original file (can regex give you location of match?)
#print words in alphabetic order, with other attributes

import re
import json

class Location(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class WordIndex(object):
    def __init__(self, word, length, count, locations):
        self.word = word
        self.length = length
        self.count = count
        self.locations = locations

expr = re.compile('([a-zA-Z]+)')

with open('testdata\wordsfile.txt', 'r') as f:
    wordDict = {}  #dictionary to keep each word (key) and attributes (WordIndex)
    text = f.read()  #read entire file, large files will need chunking

for m in expr.finditer(text):
    matchText = m.group().lower()  #lower to ensure case is ignored
    if matchText not in wordDict:
        #add to dictionary
        wordDict[matchText] = WordIndex(matchText, len(matchText), 1, [Location(m.start(), m.end())])
    else:
        #update attributes of existing item in dictionary
        item = wordDict.get(matchText)
        item.count += 1  #increment word count
        item.locations.append(Location(m.start(), m.end()))  #add another location

sortedKeys = sorted(wordDict)
for k in sortedKeys:
    val = wordDict[k]
    print(k, val.length, val.count)
    for l in val.locations:
        print(" location: {0}, {1}".format(l.start, l.end))

jsonText = json.dumps(wordDict, default=lambda o: o.__dict__)#wordDict.__dict__)
print(jsonText)

#write json to file
with open('out.txt', 'w') as fout:
    fout.write(jsonText)
