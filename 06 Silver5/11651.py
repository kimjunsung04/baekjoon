import sys

n = int(input())
nList = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

nList.sort(key=lambda x : (x[1], x[0]))

for item in nList:
    print(item[0], item[1])