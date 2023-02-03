from collections import Counter

n_list = sorted(int(input()) for _ in range(int(input())))

print(round(sum(n_list)/len(n_list)))
print(n_list[len(n_list)//2])
high_list = Counter(n_list).most_common(3)
if len(high_list) > 1 and high_list[0][1] == high_list[1][1]:
    print(high_list[1][0])
else:
    print(high_list[0][0])
print(n_list[-1]-n_list[0])