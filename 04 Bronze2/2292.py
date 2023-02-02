n = int(input())

sum_val = 1

for i in range(1000000000):
    sum_val += 6*i
    if n == 1:
        print(1)
        break
    elif sum_val >= n:
        print(i+1)
        break