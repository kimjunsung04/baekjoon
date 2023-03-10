from sys import stdin

n_list = [stdin.readline().strip() for _ in range(5)]

for j in range(15):
    for i in range(5):
        if j < len(n_list[i]):
            print(n_list[i][j], end='')