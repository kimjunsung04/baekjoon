n = int(input())

nList = map(int, input().split())

count = 0

for item in nList:
    if item >= 2:
        for i in range(2, item):
            if item % i == 0:
                break
        else:
            count += 1

print(count)