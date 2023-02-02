import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split());

queue = deque(list(range(1, n+1)))
result = []

while queue:
    for _ in range(k-1):
        queue.append(queue.popleft())
    result.append(queue.popleft())

print(f"<{', '.join(map(str,result))}>")