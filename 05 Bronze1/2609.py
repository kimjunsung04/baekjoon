a,b=map(int, input().split())
aa,bb=a, b

while a%b!=0:
    a,b=b,a%b

print(f"{b}\n{aa*bb//b}")