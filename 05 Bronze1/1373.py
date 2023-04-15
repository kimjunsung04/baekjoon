n = input()[::-1]

if len(n)%3!=0:
    n+="0"*(3-len(n)%3)

sum_val=0
p_val = ""
for i in range(len(n)+1):
    if i % 3 == 0 and i!=0:
        p_val += str(sum_val)
        sum_val=0
    if len(n) <= i: break
    if n[i] == "1": sum_val+=2**(i%3)

print(p_val[::-1])