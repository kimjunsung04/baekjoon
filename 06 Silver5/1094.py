x = int(input())

cmList = [64]

while sum(cmList) > x:
    tempMinCM = min(cmList) # 가장 작은 막대
    cmList.pop(cmList.index(tempMinCM)) # 기존 작은막대 지우고
    cmList.append(tempMinCM/2) # 자른 막대 하나를 넣음
    if sum(cmList) < x: # 이때 막대의 길이의 합이 X보다 크거나 같다면 자른 막대의 절반 중 하나를 버린다.(역조건)
        cmList.append(tempMinCM/2) # 역조건이므로 x가 더 크다면 자른 나머지도 추가해준다.

print(len(cmList))