pointInput = int(input())

if pointInput <= 100 and pointInput >= 90:
    print("A")
elif pointInput <= 89 and pointInput >= 80:
    print("B")
elif pointInput <= 79 and pointInput >= 70:
    print("C")
elif pointInput <= 69 and pointInput >= 60:
    print("D")
else:
    print("F")