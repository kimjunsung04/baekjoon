n = int(input())

packVal = 1
countVal = 0

for i in range(1, n+1):
    packVal *= i

for item in str(packVal)[::-1]:
    if item == "0": countVal += 1
    else:
        print(countVal)
        break