def getTens(num):
    numWords = ["zero","one","two","three","four","five","six","seven","eight","nine","ten" ]
    s = numWords[num]
    return s

def getTeens(num):
    numWords = ["eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
    s = numWords[num - 11]
    return s

def getUnderTwenty(num):
    if num <= 10:
        s = getTens(num)
    else:
        s = getTeens(num)
    return s

def get20to99(num):
    numWords = ["twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
    numStr = str(num)
    tens = numStr[0]
    s = numWords[int(tens) - 2]
    s = s + getTens(int(numStr[1]))
    return s

def getWordFromNumber(num):
    if num < 20:
        word = getUnderTwenty(num)
    elif num >= 20 and num < 100:
        word = get20to99(num)
    return word


while(True):

    text = input("Enter a number:")
    if text == "q":
        break
    num = int(text)

    word = getWordFromNumber(num)
    print(word)