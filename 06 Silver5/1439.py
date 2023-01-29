s = input()

for _ in range(len(s)//2):
    s = s.replace("00", "0").replace("11", "1")

print(s.count("0") if s.count("0") < s.count("1") else s.count("1"))