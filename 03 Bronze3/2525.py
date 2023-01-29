a, b = map(int, input().split())
m = int(input())

if b+m > 59:
    a += (b+m)//60
    b = (b+m)%60
else:
    b += m
if a > 23:
    a = a-24
print(f"{a} {b}")