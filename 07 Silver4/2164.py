from collections import deque

n = int(input())
nList = deque(list(range(1, n+1)))

while len(nList) > 1:
    nList.popleft()
    tempN = nList.popleft()
    nList.append(tempN)

print(nList[0])