from collections import deque

card_list = deque(range(1, int(input())+1))

while card_list:
    print(card_list.popleft(), end=" ")
    if not card_list: break
    card_list.append(card_list.popleft())