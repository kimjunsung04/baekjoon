map_list = [list(map(int, input().split())) for _ in range(9)]

max_val = [-1]

for item in map_list:
    if max(item) > max_val[0]:
        max_val = [max(item), [map_list.index(item)+1, item.index(max(item))+1]]

print(f"{max_val[0]}\n{max_val[1][0]} {max_val[1][1]}")