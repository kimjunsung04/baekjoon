a, b = map(int, input().split())
party = a * b
for i in list(map(int, input().split())):
    print(i - party, end=' ')