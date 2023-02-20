from sys import stdin

while True:
    a, b, c = map(str, stdin.readline().split())
    if a == "#": break
    if int(b) > 17 or int(c) >= 80:
        print(f"{a} Senior")
    else:
        print(f"{a} Junior")