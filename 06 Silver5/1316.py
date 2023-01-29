import math

n = int(input())

countVal = 0

for _ in range(n):
    tempInputList = list(input())
    tempGroupDict = {}
    for i in range(len(tempInputList)):
        if tempInputList[i] not in tempGroupDict:
            tempGroupDict[tempInputList[i]] = []
        if len(tempGroupDict[tempInputList[i]]) >= 1 and i-tempGroupDict[tempInputList[i]][-1] > 1:
            tempGroupDict = {}
            break
        tempGroupDict[tempInputList[i]].append(i)
    if len(tempGroupDict) != 0:
        countVal += 1

print(countVal)