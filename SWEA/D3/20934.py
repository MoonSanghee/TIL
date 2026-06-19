T = int(input())
# 테스트 케이스의 개수를 받아줍니다
for t in range(T):
    S, K = input().split()
    K = int(K)
    ball = S.index('o')
    # 최초 놓아진 형태와 이동 횟수를 받고 공의 위치를 담아줍니다
    if K == 0:
        result = ball
    elif ball == 1:
        if K % 2:
            result = 0
        else:
            result = 1
    else:
        if K % 2:
            result = 1
        else:
            result = 0
    # 이동을 하였는지 확인하고 이동 하였다면 최초 위치에 따라 결과를 구해줍니다
    print(f'#{t + 1} {result}')
    # 결과를 주어진 양식에 맞게 출력해줍니다