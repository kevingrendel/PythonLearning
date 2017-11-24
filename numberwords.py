def getTens(num):
    numWords = ["zero","one","two","three","four","five","six","seven","eight","nine","ten" ]
    s = numWords[num]
    return s

def getTeens(num):
    numWords = ["eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
    s = numWords[num - 11]
    return s

def getUnderTwenty(num):
    if num < 10:
        s = getTens(num)
    s = getTeens(num)
    return s

while(True):

    text = input("Enter a number:")
    if text == "q":
        break
    num = int(text)

    if num <= 10:
        word = getTens(num)
    elif num < 20:
        word = getUnderTwenty(num)

    print(word)
#print(num)