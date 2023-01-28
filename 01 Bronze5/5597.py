listStudent = [int(input()) for _ in range(28)]

noList = [i for i in range(1, 31) if i not in listStudent]

print(f"{min(noList)}\n{max(noList)}")