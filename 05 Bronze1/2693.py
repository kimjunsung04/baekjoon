from sys import stdin

for _ in range(int(input())):
    temp_list = sorted(list(map(int, stdin.readline().split())))
    print(temp_list[-3])