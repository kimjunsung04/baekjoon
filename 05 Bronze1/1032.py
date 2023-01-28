n = int(input())

fileList = []
finallStr = ""

while n>0:
    fileList.append(input())
    n-=1

for item in fileList:
    if finallStr == "": finallStr = item
    for i in range(len(item)):
        if list(item)[i] != finallStr[i]:
            tempFinallStrList = list(finallStr)
            tempFinallStrList[i] = "?"
            finallStr = ''.join(tempFinallStrList)

print(finallStr)