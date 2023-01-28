a, b = map(int, input().split())

tempList = []

for i in range(1, b+1):
    tempList.extend(i for _ in range(i))
print(sum(tempList[a-1:b]))