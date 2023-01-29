from itertools import permutations

n, m = map(int, input().split())

nList = list(map(int, input().split()))

sumList = []

for i in permutations(nList, 3):
    tempSum = i[0]+i[1]+i[2]
    if tempSum <= m:
        sumList.append(tempSum)

print(max(sumList))