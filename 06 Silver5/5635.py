from sys import stdin
n_list = [stdin.readline().strip().split() for _ in range(int(input()))]

for i in range(len(n_list)):
    n_list[i] = [n_list[i][0]]+list(map(int, n_list[i][1:]))

n_list.sort(key=lambda x: [x[3:], x[2], x[1]])
print(n_list[-1][0])
print(n_list[0][0])