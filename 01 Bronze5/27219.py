n = int(input())
v_count, i_count = divmod(n, 5)
result = "V" * v_count + "I" * i_count
print(result)
