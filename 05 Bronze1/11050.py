n, k = map(int, input().split())

def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)

print(factorial(n) // (factorial(k) * factorial(n - k)))