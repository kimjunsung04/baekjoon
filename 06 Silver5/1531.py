import itertools
from sys import stdin

n, m = map(int, stdin.readline().split())
temp_list = [[0 for _ in range(100)] for _ in range(100)]
for _ in range(n):
    x1, y1, x2, y2 = map(int, stdin.readline().split())
    for i, j in itertools.product(range(x1, x2+1), range(y1, y2+1)):
        temp_list[i-1][j-1] += 1

cnt = 0
for i in range(100):
    for j in range(100):
        if temp_list[i][j] > m:
            cnt += 1
print(cnt)