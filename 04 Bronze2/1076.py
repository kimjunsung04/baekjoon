jh_dict = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9,
}

sum_str = ""

for i in range(3):
    temp_input = input()
    if jh_dict[temp_input] == 0 and i == 2: continue
    sum_str += "0"*jh_dict[temp_input] if i == 2 else str(jh_dict[temp_input])
print(int(sum_str))