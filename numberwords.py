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
    s = s + " " + getTens(int(numStr[1]))
    return s

def getBase10(num, word, base):
    baseNum = num // base
    word = getWordFromRanges(baseNum) + word + getWordFromRanges(num - (baseNum*base))
    return word

def getWordFromRanges(num):
    word = ""
    if num < 20:
        word = getUnderTwenty(num)
    elif num >= 20 and num < 100:
        word = get20to99(num)
    elif num >= 100 and num < 1000:
        word = getBase10(num, " hundred ", 100)
    elif num >= 1000 and num < 1000000:
        word = getBase10(num, " thousand ", 1000)
    elif num >= 1000000 and num < 1000000000:
        word = getBase10(num, " million ", 1000000)
    elif num >= 1000000000 and num < 1000000000000:
        word = getBase10(num, " billion ", 1000000000)
    elif num >= 1000000000000 and num < 1000000000000000:
        word = getBase10(num, " trillion ", 1000000000000)
    else:
        word = "too big!"

    if len(word) > 4 and word.endswith("zero"):
        word = word.replace("zero", "")
    return word

def getWordFromNumber(num):
    return getWordFromRanges(num)


while(True):

    text = input("Enter a whole number:")
    if text == "q":
        break

    try:
        num = abs(int(text))
        word = getWordFromNumber(num)
        print(word)
    except:
        print("only whole numbers allowed.")