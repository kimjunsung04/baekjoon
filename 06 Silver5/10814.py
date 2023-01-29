n = int(input())

userList = []

for _ in range(n):
    inputVal = input().split()
    userList.append([int(inputVal[0]), inputVal[1]])

userList.sort(key=lambda x:x[0])

for item in userList:
    print(f"{item[0]} {item[1]}")