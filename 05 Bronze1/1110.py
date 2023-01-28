orgNum = input()
count = 0

if int(orgNum) < 10:
    orgNum += "0"

oNum = int(orgNum[0])
tNum = int(orgNum[-1])

while True:
    temptNum = tNum
    tNum = int(str(oNum + tNum)[-1])
    oNum = temptNum
    count += 1
    if str(oNum)+str(tNum) == str(orgNum):
        break

print(count)