from sys import stdin

n, m = map(int, input().split())

mon_list = {}

for i in range(n):
    temp_input = stdin.readline().strip()
    mon_list[str(i+1)] = temp_input
    mon_list[temp_input] = i+1

for _ in range(m):
    temp_input = stdin.readline().strip()
    print(mon_list[temp_input])