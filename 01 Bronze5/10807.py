import sys

n = int(input())

nList = list(map(int, sys.stdin.readline().split()))

v = int(input())

print(nList.count(v))