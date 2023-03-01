from sys import stdin

_ = input()
nlist = sorted(set(map(int, stdin.readline().split())))
print(' '.join(map(str, nlist)))