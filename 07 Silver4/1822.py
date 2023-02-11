from sys import stdin

an, bn = map(int, stdin.readline().split())
a_set = set(map(int, stdin.readline().split()))
b_set = set(map(int, stdin.readline().split()))

ab_set = sorted(a_set-b_set)

print(len(ab_set))
print(' '.join(list(map(str, ab_set))))