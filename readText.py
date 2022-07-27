import random as rnd

sideOneText = open('sideOne.txt', 'r')
sideTwoText = open('sideTwo.txt', 'r')

terms = sideOneText.readlines()
definitions = sideTwoText.readlines()
numTerms = len(terms)

indexArray = list(range(0, numTerms))

while indexArray:
    rand = rnd.choice(indexArray)
    print(terms[rand])
    input("click 'enter'\n")
    print(definitions[rand])
    input("click 'enter'\n")
    indexArray.remove(rand)