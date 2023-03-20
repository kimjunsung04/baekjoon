sum_val = 0

while True:
    try:
        temp_input = input()
    except EOFError:
        break
    if temp_input.startswith("gum gum") and temp_input.endswith("jay jay"): sum_val+=1
print(sum_val)