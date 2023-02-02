import sys

_ = int(input())
n_list = map(int, sys.stdin.readline().split())

_ = int(input())
m_list = map(int, sys.stdin.readline().split())

show_hash = {}
for item in n_list:
    if item in show_hash:
        show_hash[item] += 1
    else:
        show_hash[item] = 1

print(' '.join(str(show_hash[item]) if item in show_hash else '0' for item in m_list))