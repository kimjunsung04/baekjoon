n_list = [int(input()) for _ in range(3)]
if sum(n_list) != 180:
    print("Error")
elif len(set(n_list)) == 1 and n_list[0] == 60:
    print("Equilateral")
elif len(set(n_list)) == 2:
    print("Isosceles")
else:
    print("Scalene")
