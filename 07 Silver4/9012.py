import sys

n = int(input())

for _ in range(n):
    temp_input = sys.stdin.readline().strip()
    for _ in range(len(temp_input)//2):
        temp_input = temp_input.replace("()", "")
    if not temp_input:
        print("YES")
    else:
        print("NO")