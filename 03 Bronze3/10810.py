n, m = map(int, input().split())
arr = [0]*n
for _ in range(m):
    i, j, k = map(int, input().split())
    for y in range(i, j+1):
        arr[y-1] = k
for x in range(n):
    print(arr[x], '', end='')
