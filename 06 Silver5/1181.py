n = int(input())

strList = [input() for _ in range(n)]
strList = sorted(set(strList))
strList = sorted(strList, key=len)

print('\n'.join(strList))