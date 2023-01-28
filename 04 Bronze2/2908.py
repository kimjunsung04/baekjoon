abList = list(map(str, input().split()))

print(max(int(item[::-1]) for item in abList))