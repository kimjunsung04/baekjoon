n_dict = {i:0 for i in range(97, 123)}

for item in input():
    n_dict[ord(item)] += 1

print(*n_dict.values())