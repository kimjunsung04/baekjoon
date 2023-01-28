c = int(input())

pointList = [list(map(int, input().split())) for _ in range(c)]

for item in pointList:
    sumPoint = sum(item[1:])/item[0]
    tempList = [item2 for item2 in item[1:] if sumPoint < item2]
    viewStr = str(round(len(tempList)/item[0]*100, 3))
    if len(viewStr.split(".")[1]) != 3:
        print(f"{viewStr}"+("0"*(3-len(viewStr.split(".")[1])))+"%")
    else:
        print(f"{viewStr}%")