mainList = []

i = int(input())
while i > 0:
    mainList.append(int(input()))
    i -= 1

for item in sorted(mainList):
    print(item)