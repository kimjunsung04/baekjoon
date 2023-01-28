enStr = list(input())

showList = []

for item in enStr:
    if item.islower():
        showList.append(item.upper())
    else:
        showList.append(item.lower())

print(''.join(showList))