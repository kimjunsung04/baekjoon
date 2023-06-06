from sys import stdin

dic = {}
for _ in range(int(input())):
    a, b = stdin.readline().split()
    dic[a] = b
    if b == "leave":
        del dic[a]
for i in dict(sorted(dic.items(), reverse=True)):
    print(i)
