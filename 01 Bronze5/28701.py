n = int(input())
sum_val = sum(i for i in range(1, n + 1))
print(sum_val)
print(sum_val**2)
sum_szg = 0
for i in range(1, n + 1):
    sum_szg += i**3
print(sum_szg)
