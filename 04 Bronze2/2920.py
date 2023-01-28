numList = list(map(int, input().split()))

ascList = list(range(1, 9))
desList = list(range(8, 0, -1))

if numList == ascList:
	print("ascending")
elif numList == desList:
	print("descending")
else:
	print("mixed")