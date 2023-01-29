n = int(input())

count = 1

nowTitle = 666

while True:
    if nowTitle != 666 and "666" in str(nowTitle):
        count += 1
    if count >= n:
        break

    nowTitle += 1
print(nowTitle)