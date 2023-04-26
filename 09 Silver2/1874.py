n = int(input())
stack_list = []
answer = []
fg = 0
cur = 1
for _ in range(n):
    temp_input = int(input())
    while cur <= temp_input:
        stack_list.append(cur)
        answer.append("+")
        cur += 1
    if stack_list[-1] == temp_input:
        stack_list.pop()
        answer.append("-")
    else:
        print("NO")
        fg = 1
        break
if fg == 0:
    for i in answer:
        print(i)
