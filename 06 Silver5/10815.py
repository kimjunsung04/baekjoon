import sys

n = int(sys.stdin.readline())

nList = sorted(list(map(int, sys.stdin.readline().split())))

m = int(sys.stdin.readline())

mList = list(map(int, sys.stdin.readline().split()))

for item in mList:
    low, high = 0, n-1
    exist = False
    while low <= high:
        mid = (low + high) // 2
        if nList[mid] > item:
            high = mid - 1
        elif nList[mid] < item:
            low = mid + 1
        else:
            exist = True
            break
    print(1 if exist else 0, end=' ')