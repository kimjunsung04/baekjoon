n, w, h, l = map(int, input().split())
print(min((w//l)*(h//l), n))