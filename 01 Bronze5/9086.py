n = int(input())
strList = [input() for _ in range(n)]

for item in strList:
	print(f"{item[0]}{item[-1]}")