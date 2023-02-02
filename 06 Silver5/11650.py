import sys

n = int(input())
nList = sorted(list(map(int, sys.stdin.readline().split())) for _ in range(n))

for item in nList:
    print(item[0], item[1])