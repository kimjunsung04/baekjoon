import itertools
import sys

n, m = map(int, input().split())

map_list = [sys.stdin.readline().strip() for _ in range(n)]

map_a = [
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
]

map_b = [
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
]

show_list = []

def check_map(map_list):
    count = [0, 0]
    for i, j in itertools.product(range(8), range(8)):
        if map_list[i][j] == map_a[i][j]: count[0] += 1
        if map_list[i][j] == map_b[i][j]: count[1] += 1
    return min(count)

for i, j in itertools.product(range(n-7), range(m-7)):
    temp_map = []
    for ii in range(8):
        temp_line = "".join(map_list[ii+i][jj+j] for jj in range(8))
        temp_map.append(temp_line)
    show_list.append(check_map(temp_map))

print(min(show_list))