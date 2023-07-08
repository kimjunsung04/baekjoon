ds, ys = map(int, input().split())
dm, ym = map(int, input().split())

for i in range(5000):
    if (i + ds) % ys == 0 and (i + dm) % ym == 0:
        print(i)
        break
