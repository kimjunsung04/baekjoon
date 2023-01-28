import sys

n, m = map(int, sys.stdin.readline().split())

oneList = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
twoList = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

showList = []

for i in range(n):
    tempList = [oneList[i][j]+twoList[i][j] for j in range(m)]
    showList.append(tempList)

for i in range(n):
    for j in range(m):
        print(f"{showList[i][j]} ", end="")
    print()