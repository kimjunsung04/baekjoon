a, b, n = map(int, input().split())

for _ in range(n):
    a = (a%b)*10
    result = a//b

print(result)