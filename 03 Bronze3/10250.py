for _ in range(int(input())):
    h, _, n = map(int, input().split())
    print(100*((n-1)%h+1)+(n-1)//h+1)