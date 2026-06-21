T = int(input())
# 주어지는 테스트케이스가 몇개인지 받아줍니다
for t in range(T):
    S = input()
    front = S[:(len(S) - 1) // 2]
    back = S[(len(S) - 1) // 2 + 1 :]
    # 단어를 받고 확인할 앞, 뒤 영역을 변수에 담아줍니다
    flag = True
    # 주어진 조건이 모두 성립하는지를 확인할 변수를 설정해줍니다
    if S != S[::-1]:
        flag = False
    elif front != front[::-1]:
        flag = False
    elif back != back[::-1]:
        flag = False
    # 주어진 조건이 모두 성립하는지 확인해줍니다
    if flag:
        print(f'#{t + 1} YES')
    else:
        print(f'#{t + 1} NO')
    # 결과를 주어진 양식에 맞게 출력해줍니다