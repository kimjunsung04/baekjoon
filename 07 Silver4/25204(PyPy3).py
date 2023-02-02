import sys
from functools import cmp_to_key
def custom_sort(x, y):
    if x == y: return 0
    elif x.startswith(y): return 1
    elif y.startswith(x): return -1
    else:
        for i in range(min(len(x), len(y))):
            if x[i] != y[i]:
                if x[i] == '-' and y[i] != '-': return 1
                elif x[i] != '-' and y[i] == '-': return -1
                elif x[i].isalpha() and y[i].isalpha():
                    if x[i].upper() == y[i].upper(): return 1 if x[i].islower() else -1
                    else: return (ord(x[i].upper()) - ord(y[i].upper()))
                else: return (ord(x[i]) - ord(y[i]))
        return len(x) - len(y)
t = int(input())
for _ in range(t):
    n = int(input())
    strings = [sys.stdin.readline().strip() for _ in range(n)]
    strings = sorted(strings, key=cmp_to_key(custom_sort))
    for string in strings: print(string)