m = int(input())
n = int(input())

showList = []

for i in range(m, n+1):
    if i >= 2:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            showList.append(i)

if not showList:
    print(-1)
else:
    print(f"{sum(showList)}\n{min(showList)}")