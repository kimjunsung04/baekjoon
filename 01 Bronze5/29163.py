_ = input()
h, z = 0, 0
for item in map(int, input().split()):
    if item % 2 == 0:
        z += 1
    else:
        h += 1
print("Sad" if h >= z else "Happy")
