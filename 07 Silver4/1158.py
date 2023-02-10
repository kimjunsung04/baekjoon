from collections import deque

n, k = map(int, input().split())

n_list = deque(list(range(1, n+1)))
result = []

while n_list:
    for _ in range(k-1):
        n_list.append(n_list.popleft())
    result.append(n_list.popleft())

print(str(result).replace("[", "<").replace("]", ">"))