input_val = int(input())
num_val = 0

for i in range(1, input_val+1):
    if i < 100:
        num_val += 1
    else:
        i_list_val = list(map(int, str(i)))
        if i_list_val[0]-i_list_val[1] == i_list_val[1]-i_list_val[2]:
            num_val+=1

print(num_val)