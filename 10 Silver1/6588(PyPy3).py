from sys import stdin

array = [True for _ in range(1000001)]

for i in range(2, 1001):
    if array[i]:
        for k in range(i + i, 1000001, i):
            array[k] = False

while True:
    n = int(stdin.readline())
    if n == 0: break
    for i in range(3, len(array)):
        if array[i] and array[n-i]:
            print(f"{n} = {i} + {n-i}")
            break