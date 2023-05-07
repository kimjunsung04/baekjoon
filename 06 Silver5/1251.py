n = input()
n_list = []

for i in range(1, len(n)):
    for j in range(i+1, len(n)):
        t1 = n[:i][::-1]
        t2 = n[i:j][::-1]
        t3 = n[j:][::-1]
        n_list.append(t1+t2+t3)

print(sorted(n_list)[0])
