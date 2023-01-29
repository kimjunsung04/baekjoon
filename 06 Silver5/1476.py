e, s, m = map(int, input().split())

ee, ss, mm = 0, 0, 0

yearVal = 0

while True:
    yearVal += 1
    if ee >= 15: ee = 1
    else: ee += 1
    if ss >= 28: ss = 1
    else: ss += 1
    if mm >= 19: mm = 1
    else: mm += 1
    if e == ee and s == ss and m == mm:
        print(yearVal)
        break