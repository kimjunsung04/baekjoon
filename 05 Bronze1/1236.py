n, m = map(int,input().split())
board = [input() for _ in range(n)]

a, b = 0, 0

for i in range(n): # 가로 체크
    if "X" not in board[i]:
        a += 1

for j in range(m): # 세로 체크
    if "X" not in [board[i][j] for i in range(n)]: # board[i][j]를 리스트에 넣어서 "X"가 없는지 체크
        b += 1

print(max(a, b))