x, y, w, h = map(int, input().split())

mapList = [[0 for _ in range(w)] for _ in range(h)]

# 현재좌표 왼쪽까지 거리
# x

# 현재좌표 오른쪽까지 거리
# w-x

# 현재좌표 위쪽까지 거리
# y

# 현재좌표 아래까지 거리
# h-y
print(min([x, w-x, y, h-y]))