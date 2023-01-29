strInput = input()

for item in ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]:
    strInput = strInput.replace(item, "0")

print(len(strInput))