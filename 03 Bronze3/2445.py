n = int(input())

for i in range(n-1, 0, -1):
    print("*"*(n-i) + " "*(i-1) + " "*(i+1) + "*"*(n-i))
for i in range(1, n+1):
    print("*"*(n-i+1) + " "*(i-1) + " "*(i-1) + "*"*(n-i+1))
