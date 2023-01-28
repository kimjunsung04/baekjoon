abcList = [int(input()) for _ in range(3)]

abcMultiply = abcList[0] * abcList[1] * abcList[2]

for i in range(10):
    print(str(abcMultiply).count(f"{i}")) 