import sys

n = int(sys.stdin.readline())

nList = sorted([int(sys.stdin.readline()) for _ in range(n)])

for item in nList:
    print(item)