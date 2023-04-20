numberList = [3, 7, 2, 1]
highNum = 0

#for x in range(0, len(numberList) - 1):
#    if numberList[x] < numberList[x + 1]:
#        highNum = numberList[x + 1]
#print(highNum)

for x in numberList:
    if x > highNum:
        highNum = x

print(highNum)