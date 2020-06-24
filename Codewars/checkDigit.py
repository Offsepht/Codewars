def calculateCheckDigit(num):
    listOfNum = list(num)
    newList = []
    newList2 = []

    for i in listOfNum[::2]:
        newList.append(int(i))

    for i in listOfNum[1::2]:
        newList2.append(int(i))

    print(sum(newList) * 3)
    print(sum(newList2))
    x = (sum(newList) * 3) + sum(newList2)
    x = x % 10
    print(x)
    #return num + str(x)



print(calculateCheckDigit('75658918277'))
print(calculateCheckDigit('88346601030')) #7
print(calculateCheckDigit('88346601577'))