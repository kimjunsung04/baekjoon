n = int(input())

bag = 0

while n >= 0:
    if n % 5 == 0:
        bag += n//5
        print(bag)
        break
    bag += 1
    n -= 3
else:
    print(-1)