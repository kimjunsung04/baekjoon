gyList = list(map(int, input().split()))

print(sum(item*item for item in gyList)%10)