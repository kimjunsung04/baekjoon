from sys import stdin

money_deque = []

for _ in range(int(input())):
    temp_input = int(stdin.readline())
    if temp_input == 0 and money_deque:
        money_deque.pop()
        continue
    money_deque.append(temp_input)

print(sum(money_deque))