orgStrList = list(input().upper())

indexVal = []
contentVal = []

for item in set(orgStrList):
    indexVal.append(orgStrList.count(item))
    contentVal.append(item)

if indexVal.count(max(indexVal)) > 1:
    print("?")
else:
    print(contentVal[indexVal.index(max(indexVal))])