x = int(input())

lineVal = 0
endVal = 0

while x > endVal:
    lineVal += 1
    endVal += lineVal

gapVal = endVal - x

if lineVal % 2 == 0:
    topVal = lineVal - gapVal
    bottomVal = gapVal + 1
else:
    topVal = gapVal + 1
    bottomVal = lineVal - gapVal

print(f"{topVal}/{bottomVal}")