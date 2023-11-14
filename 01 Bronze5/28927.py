t1, e1, f1 = map(int, input().split())
t2, e2, f2 = map(int, input().split())
max_time = t1 * 3 + e1 * 20 + f1 * 120
min_time = t2 * 3 + e2 * 20 + f2 * 120
if max_time == min_time:
    print("Draw")
elif max_time > min_time:
    print("Max")
elif min_time > max_time:
    print("Mel")
