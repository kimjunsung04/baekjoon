n = int(input())

strList = [input().split() for _ in range(n)]

for item in strList:
    tempList = [item2[::-1] for item2 in item]
    print(' '.join(tempList))