import sys

n = int(input())

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)