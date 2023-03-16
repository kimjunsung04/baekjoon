n, k = int(input()), int(input())
start, end = 1, k

while start <= end:
    mid = (start + end) // 2

    temp = sum(min(mid//i, n) for i in range(1, n+1))
    if temp >= k:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1
print(answer)
