sInput = input()

azSet = [chr(i) for i in range(ord("a"), ord("z")+1)]

for item in azSet:
	if sInput.count(item) > 0:
		print(f'{list(sInput).index(f"{item}")} ', end="")
	else:
		print("-1 ", end="")