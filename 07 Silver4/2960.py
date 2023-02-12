n, k = map(int, input().split())

n_list = list(range(2, n+1))
count_val = 0
while n_list:
    p = min(n_list)
    temp_list = []
    for item in n_list:
        if item >= p and item % p == 0:
            n_list.remove(item)
            count_val+=1
        if count_val==k:
            print(item)
            break
    if count_val==k:
        break