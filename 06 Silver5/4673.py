def d(n):
    return n+sum(map(int, str(n)))

showList = [d(i) for i in range(1, 10000)]
for i in range(1, 10000):
    if i not in showList:
        print(i)