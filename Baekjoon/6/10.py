# 6-10 문제번호 1316

a = int(input())
c = a
for i in range(a):
    b = list(input())
    for j in range(len(b) - 1):
        if b[j] == b[j + 1]:
            pass
        elif b[j] in b[j+1:]:
            c -= 1
            # b의 j번에 위치한 문자가 b의 j번 다음부터의 문자열에 포함되면 
            # 그룹 단어가 아니기때문에 이 경우마다 입력해준다고 선언한 그룹 단어수에서 1씩빼준다.
            break
print(c)