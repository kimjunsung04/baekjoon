n = int(input())

nList = [list(map(str, input().split())) for _ in range(n)]

for item in nList:
    for strItem in item[1]:
        print(int(item[0])*strItem, end="")
    print("")