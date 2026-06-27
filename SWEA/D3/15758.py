T = int(input())
# 테스트케이스의 개수를 받아줍니다
for t in range(T):
    S, T = input().split()
    S, T = S * len(T), T * len(S)
    # 주어지는 두 단어를 받고 같은 길이가 되도록 다른 단어의 길이만큼 반복하여줍니다
    if S == T:
        print(f'#{t + 1} yes')
    else:
        print(f'#{t + 1} no')
    # 두 단어가 같은지 확인하여 결과를 출력해줍니다