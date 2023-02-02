def sosu_ch(num):  # sourcery skip: invert-any-all, use-any
    if num==1: return False
    for i in range(2, int(num**0.5)+1):
        if num%i == 0: return False
    return True

for _ in range(int(input())):
    temp_input = int(input())
    a, b = temp_input//2, temp_input//2
    while a>0:
        if sosu_ch(a) and sosu_ch(b):
            print(a, b)
            break
        else:
            a-=1
            b+=1