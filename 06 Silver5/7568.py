n = int(input())

dList = [list(map(int, input().split())) for _ in range(n)]

for i in dList:
    rank = 1 + sum(i[0] < j[0] and i[1] < j[1] for j in dList)
    print(rank, end = " ")