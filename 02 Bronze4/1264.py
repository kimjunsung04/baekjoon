contentList = []

while True:
    tempInput = input()
    if tempInput == "#": break
    contentList.append(tempInput)

for item in contentList:
    tempED = sum(item.lower().count(item2) for item2 in ['a', 'e', 'i', 'o', 'u'])
    print(tempED)

print()