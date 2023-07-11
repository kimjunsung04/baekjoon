for _ in range(int(input())):
    g, c, e = map(int, input().split())
    km = [1, 3, 5]
    candies_needed = max(0, e - c)
    result = candies_needed * km[g-1]
    print(result)
