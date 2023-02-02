import sys

stack = []

for _ in range(int(input())):
    temp_input = sys.stdin.readline().strip()
    if "push" in temp_input:
        temp_num_val = temp_input[5:]
        stack.append(temp_num_val)
    elif "pop" in temp_input:
        if stack: 
            print(stack[-1])
            stack.pop(-1)
        else: print(-1)
    elif "size" in temp_input:
        print(len(stack))
    elif "empty" in temp_input:
        if not stack: print(1)
        else: print(0)
    elif not stack: print(-1)
    else: print(stack[-1])