malList = list(map(int, input().split()))

setList = [1,1,2,2,2,8]

for i in range(6):
    if setList[i] == malList[i]:
        print(0, end=" ")
    else:
        print(setList[i]-malList[i], end=" ")