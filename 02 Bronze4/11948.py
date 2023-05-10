n_list = [int(input()) for _ in range(6)]
print(sum(sorted(n_list[:4])[1:]) + max(n_list[4:]))
