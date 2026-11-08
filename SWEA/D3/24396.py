T = int(input())

for _ in range(T):
    B, W, X, Y, Z = map(int, input().split())
    result = 0
    # 주어지는 변수들을 받고 결과를 담을 변수를 설정해줍니다
    result += min(B, W) * (max(Z * 2, X + Y))
    # 두 색의 공중에 적은 쪽을 기준으로 교차하여 넣는것과 옳바르게 넣는 것중 높은 점수로 득점하도록 분류합니다
    if B > W:
        result += (B - W) * X
    else:
        result += (W - B) * Y
    # 남은 공의 점수를 더해줍니다
    print(result)
    # 결과를 출력해줍니다