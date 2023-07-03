_, a, b = map(int, input().split())
if a < b:
    print("Bus")
elif a > b:
    print("Subway")
else:
    print("Anything")
