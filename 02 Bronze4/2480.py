abcList = list(map(int, input().split()))

for item in abcList:
    if abcList.count(item) == 3:
        print(10000+item*1000)
        break
    elif abcList.count(item) == 2:
        print(1000+item*100)
        break
else:
    print(max(abcList)*100)