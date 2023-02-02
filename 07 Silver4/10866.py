from sys import stdin
from collections import deque

show_deque = deque()

for _ in range(int(input())):
    temp_input = stdin.readline().strip()
    if "push_back" in temp_input:
        temp_num = temp_input[10:]
        show_deque.append(temp_num)
    elif "push_front" in temp_input:
        temp_num = temp_input[11:]
        show_deque.appendleft(temp_num)
    elif "pop_front" in temp_input:
        if show_deque: print(show_deque.popleft())
        else: print(-1)
    elif "pop_back" in temp_input:
        if show_deque: print(show_deque.pop())
        else: print(-1)
    elif "size" in temp_input:
        print(len(show_deque))
    elif "empty" in temp_input:
        print(0 if show_deque else 1)
    elif "front" in temp_input:
        print(show_deque[0] if show_deque else -1)
    elif "back" in temp_input:
        print(show_deque[-1] if show_deque else -1)