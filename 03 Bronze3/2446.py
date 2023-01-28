n = int(input())

for i in range(n-1, 0, -1):
    print(" "*(n-i-1) + "*"*(i) + "*"*(i+1))
for i in range(1, n+1):
    print(" "*(n-i) + "*"*(i) + "*"*(i-1))