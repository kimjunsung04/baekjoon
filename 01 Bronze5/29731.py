gy_list = [
    "Never gonna give you up",
    "Never gonna let you down",
    "Never gonna run around and desert you",
    "Never gonna make you cry",
    "Never gonna say goodbye",
    "Never gonna tell a lie and hurt you",
    "Never gonna stop",
]
n = int(input())
word_list = [1 for _ in range(n) if input() in gy_list]
print("No" if sum(word_list) == n else "Yes")
