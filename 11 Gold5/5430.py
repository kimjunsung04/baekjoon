from collections import deque

n = int(input())

for _ in range(n):
    rdStr = input()
    tempN = int(input())
    tempList = deque(eval(input()))

    error = False
    rCount = 0
    for rd in rdStr:
        if rd == "R":
            rCount+=1
        elif rd == "D":
            if tempList:
                if rCount % 2 == 0:
                    tempList.popleft()
                else:
                    tempList.pop()
            else:
                error = True
                break
    if rCount % 2 == 1:
        tempList.reverse()
    if error:
        print("error")
    else:
        print(str(list(tempList)).replace(" ", ""))