n = int(input())

showList = []

for i in range(1, 1000000):
    if i > n: break
    tempVal = i+sum(map(int, str(i)))
    if tempVal == n:
        showList.append(i)

if not showList:
    print(0)
else:
    print(min(showList))