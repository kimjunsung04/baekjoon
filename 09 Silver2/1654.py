k, n = map(int, input().split())
lans = [int(input()) for _ in range(k)]

low = 1
high = max(lans)

while low < high:
    middle = (low+high)//2+1
    s = sum(i//middle for i in lans)
    if s >= n:
        low = middle
    else:
        high = middle-1
print(low)