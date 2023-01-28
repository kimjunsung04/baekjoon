n = int(input())

knList = [[int(input()), int(input())] for _ in range(n)]

setDict = []

for i in range(15):
    tempList = []
    for j in range(1, 15):
        if i == 0:
            tempList.append([j, j])
        else:
            tempSum = sum(item[1] for item in setDict[i-1][:j])
            tempList.append([j, tempSum])
    setDict.append(tempList)

for item in knList:
    print(setDict[item[0]][item[1]-1][1])