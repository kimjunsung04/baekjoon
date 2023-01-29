import itertools
n = int(input())

nList = [list(map(int, input().split())) for _ in range(n)]

mapList = [[0 for _ in range(100)] for _ in range(100)]

for item, i in itertools.product(nList, range(-1, 9)):
    for j in range(-1, 9):
        mapList[item[1]+i][item[0]+j] = 1

print(sum(item.count(1) for item in mapList))