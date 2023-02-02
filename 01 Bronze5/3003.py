malList = list(map(int, input().split()))

setList = [1,1,2,2,2,8]

for i in range(6):
    print(setList[i]-malList[i], end=" ")