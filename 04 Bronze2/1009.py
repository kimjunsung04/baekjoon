t = int(input())

mainList = []

for _ in range(t):
    tempA, tempB = map(int, input().split())
    tempA = tempA % 10
    if tempA == 0:
        tempED = 10
    elif tempA in [1, 5, 6]:
        tempED = tempA
    elif tempA in [4, 9]:
        tempB = tempB % 2
        tempED = tempA if tempB == 1 else (tempA * tempA) % 10
    else:
        tempB = tempB % 4
        tempED = (
            (tempA**4) % 10 % 10 % 10
            if tempB == 0
            else (tempA**tempB) % 10 % 10 % 10
        )
    mainList.append(tempED)

for item in mainList:
    print(item)