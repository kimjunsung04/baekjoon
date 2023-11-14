n = int(input())
if "7" not in str(n) and n % 7 != 0:
    print(0)
elif "7" not in str(n) and n % 7 == 0:
    print(1)
elif "7" in str(n) and n % 7 != 0:
    print(2)
elif "7" in str(n) and n % 7 == 0:
    print(3)
