from sys import stdin

n = int(input())
a_list = sorted(list(map(int, stdin.readline().split())))
b_list = list(map(int, stdin.readline().split()))

print(sum(a_list.pop(a_list.index(min(a_list)))*b_list.pop(b_list.index(max(b_list))) for _ in range(n)))