# sourcery skip: sum-comprehension, use-itertools-product
n, m = map(int, input().split())

mapList = [list(map(int, input().split())) for _ in range(n)]

k = int(input())

ijxyList = [list(map(int, input().split())) for _ in range(k)]

for ijxy in ijxyList:
    tempSum = 0
    for i in range(ijxy[0]-1, ijxy[2]):
        for j in range(ijxy[1]-1, ijxy[3]):
            tempSum += mapList[i][j]
    print(tempSum)