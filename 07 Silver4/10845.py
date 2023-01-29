import sys

n = int(input())

showList = []

for _ in range(n):
    tempInput = sys.stdin.readline()
    if "push" in tempInput:
        showList.append(int(tempInput.split()[1]))
    elif "pop" in tempInput:
        if not showList:
            print(-1)
        else:
            print(showList[0])
            showList.pop(0)
    elif "size" in tempInput:
        print(len(showList))
    elif "empty" in tempInput:
        print(0 if showList else 1)
    elif "front" in tempInput:
        if not showList: print(-1)
        else: print(showList[0])
    elif "back" in tempInput:
        if not showList: print(-1)
        else: print(showList[-1])