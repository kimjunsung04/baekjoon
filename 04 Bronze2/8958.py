n = int(input())

oxInput = [list(input()) for _ in range(n)]

for itemList in oxInput:
	sumNum = 0
	tempNum=1
	for item in itemList:
		if item == "X":
			tempNum = 1
		elif item == "O":
			sumNum+=tempNum
			tempNum+=1
	print(sumNum)