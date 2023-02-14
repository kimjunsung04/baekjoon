from sys import stdin

input_str = stdin.readline().strip()

for i in range(1, len(input_str)+1):
    if i % 10 == 0: print(input_str[i-1])
    else: print(input_str[i-1], end="")