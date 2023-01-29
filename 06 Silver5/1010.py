import math

n = int(input())

caseList = [list(map(int, input().split())) for _ in range(n)]

def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)

for case in caseList:
    bridge = math.factorial(case[1]) // (math.factorial(case[0]) * math.factorial(case[1] - case[0]))
    print(bridge)