n = list(input())


count = 1

while True:
    setList = list(range(10))

    for item in list(n): # 세트 하나 사용
        if int(item) in setList: # 만약 세트안에 원하는게 있다면
            n.remove(item) # 번호 추가했으니 리스트 제거
            setList.remove(int(item)) # 사용했으니 세트도 제거
        elif int(item) == 6 and 9 in setList: # 필요한 숫자가 6인데 세트안에 9가 있다면
            n.remove(item) # 번호 추가했으니 리스트 제거
            setList.remove(9) # 9를 제거
        elif int(item) == 9 and 6 in setList: # 필요한 숫자가 9인데 세트안에 6이 있다면
            n.remove(item) # 번호 추가했으니 리스트 제거
            setList.remove(6) # 6을 제거
    if not n: break # 원하는걸 충족했다면
    count += 1

print(count)