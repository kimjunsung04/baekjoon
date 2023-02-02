import sys

n = int(sys.stdin.readline())

nSet = set()

for _ in range(n):
    inputStr = sys.stdin.readline()
    if "add" in inputStr:
        x = int(inputStr[4:])
        if x not in nSet:
            nSet.add(x)
    elif "remove" in inputStr:
        x = int(inputStr[7:])
        if x in nSet:
            nSet.discard(x)
    elif "check" in inputStr:
        x = int(inputStr[6:])
        print(1 if x in nSet else 0)
    elif "toggle" in inputStr:
        x = int(inputStr[7:])
        if x in nSet: nSet.discard(x)
        else: nSet.add(x)
    elif "all" in inputStr:
        nSet = set(range(1, 21))
    else:
        nSet = set()