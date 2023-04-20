numList = [3, 7, 2, 1]
finalList = []

def highNum(list):
    highNumber = 0
    highNumberIndex = 0
    for x in range(0, len(list)):
        if list[x] > highNumber:
            highNumberIndex = x
            highNumber = list[x]
    return highNumberIndex

while numList != []:
    indexMaior = highNum(numList)
    sacarFora = numList.pop(indexMaior)
    finalList.append(sacarFora)

print(numList)
print(finalList)
