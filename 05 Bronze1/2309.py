nanList = [int(input()) for _ in range(9)]

for i in range(9):
    for j in range(9):
        if i != j and nanList[i] + nanList[j] == sum(nanList)-100:
            tempList = list(nanList)
            tempList.remove(nanList[i])
            tempList.remove(nanList[j])
            tempList.sort()
            nanList = tempList
            break
    if len(nanList) == 7:
        break

print('\n'.join(map(str, nanList)))