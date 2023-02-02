import sys

n, k = map(int, input().split())

aList = sorted(map(int, sys.stdin.readline().split()))

print(aList[k-1])