T = int(input())
# 주어질 단어의 개수를 받아줍니다
for _ in range(T):
    S = input()
    # 문자열을 받아줍니다
    for i in range(len(S)):
        if S[i:] == S[i:][::-1]:
            if i == 0:
                break
            # 길이가 1이상의 부분에서 뒤집어서 동일해 재활용 가능한 부분을 확인해줍니다
            S += S[i - 1::-1]
            break
            # 재활용 할 수 없어 필요한 부분을 더해줍니다
    
    print(S)
    # 새로 만들어진 문자열을 출력해줍니다