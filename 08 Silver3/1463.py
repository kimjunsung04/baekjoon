n = int(input())
tempList = [0] * (n + 1)

for i in range(2, n + 1):
    tempList[i] = tempList[i - 1] + 1
    if i % 3 == 0: tempList[i] = min(tempList[i], tempList[i // 3] + 1)
    if i % 2 == 0: tempList[i] = min(tempList[i], tempList[i // 2] + 1)
print(tempList[n])