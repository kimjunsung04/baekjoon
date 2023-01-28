import sys

n, x = map(int, sys.stdin.readline().split())

nList = map(int, sys.stdin.readline().split())

showList = [str(item) for item in nList if x > item]

print(' '.join(showList))