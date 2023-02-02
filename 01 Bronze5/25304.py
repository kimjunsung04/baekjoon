my_money = int(input())

n_list = [
    list(map(int, input().split())) for _ in range(1, int(input()) + 1)
]

if sum(i[0] * i[1] for i in n_list) == my_money:
    print("Yes")
else:
    print("No")