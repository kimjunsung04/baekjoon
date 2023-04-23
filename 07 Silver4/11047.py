n, m = map(int, input().split())
count = 0
coin_types = [int(input()) for _ in range(n)]

for coin in reversed(coin_types):
    count += m // coin
    m %= coin

print(count)
