import math

a, b = map(int, input().split())

def sosu_ck(num):  # sourcery skip: invert-any-all, use-any, use-next
    if num==1: return False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0: return False
    return True

for i in range(a, b+1):
    if sosu_ck(i): print(i)