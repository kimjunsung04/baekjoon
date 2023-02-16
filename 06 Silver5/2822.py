from sys import stdin

sc_list = [int(stdin.readline()) for _ in range(8)]

sc_list_sorted = sorted(sc_list)[3:]

print(sum(sc_list_sorted))

for item in sc_list:
    if item in sc_list_sorted:
        print(sc_list.index(item)+1, end=" ")