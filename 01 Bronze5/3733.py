while True:
    try:
        n, s = map(int, input().split())
    except EOFError:
        break
    else:
        print(s//(n+1))