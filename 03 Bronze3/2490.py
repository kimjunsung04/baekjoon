for _ in range(3):
    y_ca = list(map(int, input().split())).count(1)
    if y_ca == 3: print("A")
    elif y_ca == 2: print("B")
    elif y_ca == 1: print("C")
    elif y_ca == 0: print("D")
    elif y_ca == 4: print("E")