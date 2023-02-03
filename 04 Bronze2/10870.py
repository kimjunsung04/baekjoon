def pibo(num, num2, i, target):
    return num if i == target else pibo(num2, num+num2, i+1, target)

n = int(input())
print(pibo(0, 1, 0, n))