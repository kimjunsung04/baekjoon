import sys

n = int(input())

nList = set(list(map(int, sys.stdin.readline().split())))

m = int(input())

mList = list(map(int, sys.stdin.readline().split()))

for item in mList:
    print(1 if item in nList else 0)