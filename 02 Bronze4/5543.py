n_list = [int(input()) for _ in range(5)]

print((sorted(n_list[:3])[0] + sorted(n_list[3:])[0]) - 50)
