n = int(input())
sum_val = 0
for i in range(1, n+1):
    if i >= 100000000: sum_val+=9
    elif i >= 10000000: sum_val+=8
    elif i >= 1000000: sum_val+=7
    elif i >= 100000: sum_val+=6
    elif i >= 10000: sum_val+=5
    elif i >= 1000: sum_val+=4
    elif i >= 100: sum_val+=3
    elif i >= 10: sum_val+=2
    else: sum_val+=1
print(sum_val)