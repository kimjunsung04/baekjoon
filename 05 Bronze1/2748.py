n = int(input())

piboList = [0, 1]

piboList.extend(piboList[i-1]+piboList[i] for i in range(1, n))
print(piboList[-1])