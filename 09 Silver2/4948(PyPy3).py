def sosu_ch(num):  # sourcery skip: invert-any-all, use-any
    if num==1: return False
    for i in range(2, int(num**0.5)+1):
        if num%i == 0: return False
    return True

while True:
    temp_input = int(input())
    if temp_input == 0: break
    temp_num = sum(1 for i in range(temp_input+1, (temp_input*2)+1) if sosu_ch(i))
    print(temp_num)