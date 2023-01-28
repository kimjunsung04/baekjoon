a, b, c = map(int, input().split())

sumMoney = 0

abcList = [a, b, c]

for item in abcList:
    if abcList.count(item) == 3:
        print(10000+item*1000)
        break
    elif abcList.count(item) == 2:
        print(1000+item*100)
        break
else:
    print(max(abcList)*100)