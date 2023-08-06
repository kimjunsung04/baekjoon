a = list(map(int,input().split()))
b = [i for i in range(1,a[0]+1) if a[0]%i == 0]
if len(b) < a[1]: print(0)
else: print(b[a[1]-1])