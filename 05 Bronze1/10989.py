import sys

n = int(sys.stdin.readline())
array = [0] * 10001

for _ in range(n):
    data = int(sys.stdin.readline())
    array[data] += 1

for i in range(10001):
    if array[i] != 0:
        for _ in range(array[i]):
            print(i)