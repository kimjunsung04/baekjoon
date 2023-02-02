from sys import stdin

n, k = map(int, stdin.readline().split())
n_list = sorted(list(map(int, stdin.readline().split())))

print(n_list[-k])