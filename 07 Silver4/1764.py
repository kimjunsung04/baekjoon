from sys import stdin

n, m = map(int, input().split())

d_set = {stdin.readline().strip() for _ in range(n)}
b_set = {stdin.readline().strip() for _ in range(m)}
db_set = sorted(d_set&b_set)

print(f"{len(db_set)}\n"+'\n'.join(db_set))