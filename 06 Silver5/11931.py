from sys import stdin

n_list = sorted([int(stdin.readline()) for _ in range(int(stdin.readline()))], reverse=True)
print('\n'.join(map(str, n_list)))