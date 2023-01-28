n = int(input())

scList = list(map(int, input().split()))
newScList = [item/max(scList)*100 for item in scList]
print(sum(newScList)/n)