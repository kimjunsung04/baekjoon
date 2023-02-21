r1, s = map(int, input().split())

for i in range(-1000, 1001):
    if (r1+i)//2 == s:
        print(i)
        break