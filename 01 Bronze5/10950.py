n = int(input())

nList = [list(map(int, input().split())) for _ in range(n)]

for item in nList:
	print(item[0]+item[1])