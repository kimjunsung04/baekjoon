n = int(input())

tempNum = 2
while n != 1:
    if n % tempNum == 0:
        print(tempNum)
        n /= tempNum
        tempNum = 2
        continue
    tempNum += 1