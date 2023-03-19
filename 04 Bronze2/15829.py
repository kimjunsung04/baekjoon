l = int(input())
temp_input = input()
answer = sum((ord(temp_input[i])-96) * (31 ** i) for i in range(l))
print(answer % 1234567891)