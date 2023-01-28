strList = []

while True:
    tempInput = input()
    if tempInput == "0": break
    strList.append(tempInput)

for item in strList:
    tempStr = "".join(item[-i] for i in range(1, len(item)//2+1))
    if tempStr == item[:len(item)//2]:
        print("yes")
    else:
        print("no")