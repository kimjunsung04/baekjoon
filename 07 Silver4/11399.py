n = int(input())
p = sorted(list(map(int, input().split())))
print(sum(p[i] * (n - i) for i in range(n)))
