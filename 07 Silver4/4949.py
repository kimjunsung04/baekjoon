from sys import stdin

while True:
    temp_input = stdin.readline().replace("\n", "") # strip 사용시 " ." 에서 공백이 무시되어 replace 사용
    if temp_input == ".": break
    ghstr =''.join([i for i in list(temp_input) if i in ["(", ")", "[", "]"]])
    for _ in range(len(ghstr)//2):
        ghstr = ghstr.replace("()", "").replace("[]", "")
    if not ghstr: print("yes")
    else: print("no")