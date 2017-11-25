import re

expr = re.compile('([a-zA-Z]+)')

with open('testdata\wordsfile.txt', 'r') as f:
    #while not end of file
    #read 100 chars
    #keep lastbyteread index
    #use regex and match on alpha characters
    #read next set
    #move char by char until space or EOF is found
    #combine last char with remaining chars
    text = f.read(size)
    mText = expr.findall(text)
    print(mText)