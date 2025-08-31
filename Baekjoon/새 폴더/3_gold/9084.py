t = int(input())
# 테스트 케이스의 수를 받아줍니다
for tc in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    target = int(input())
    # 동전의 종류를 받고 목표 금액을 받아줍니다
    dp = [0] * (target + 1)
    dp[0] = 1
    # 목표금액 + 1만큼의 크기를 가지는 dp 리스트를 만들고 0번 인덱스 값을 1로 설정해줍니다
    for coin in coins:
        for i in range(1, target + 1):
            if i >= coin:
                dp[i] += dp[i - coin]
        # 동전의 개수에 제한이 없으므로 동전을 추가하여 목표 금액 이하의 금액을 만들 수 있다면 방법을 누적시켜줍니다
    print(dp[-1])
    # dp리스트에 목표 금액에 담긴 방법수를 출력해줍니다