from sys import stdin
while True:
    temp_str = stdin.readline().strip()
    if temp_str == "0":
        break
    gap_cm = 0
    for item in temp_str:
        if item == "0":
            gap_cm += 4
        elif item == "1":
            gap_cm += 2
        else:
            gap_cm += 3
    print(gap_cm+(len(temp_str)-1)+2)
