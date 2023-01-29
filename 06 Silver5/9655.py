n = int(input())

nowUser = "SK"

UserList = ["SK", "CY"]

for i in range(n):
    nowUser = UserList[i % 2]
    n -= 1 if n <= 3 else 3
    if n == 0: break

print(nowUser)