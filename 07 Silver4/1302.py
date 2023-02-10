from sys import stdin

n = int(input())
max_val = ["", 0]

book_dict = {}
for _ in range(n):
    temp_input = stdin.readline().strip()
    if temp_input not in book_dict:
        book_dict[temp_input] = 0
    book_dict[temp_input] += 1

print(sorted([k for k,v in book_dict.items() if max(book_dict.values()) == v])[0])