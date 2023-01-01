n, k = map(int, input().split())
coins = [int(input()) for i in range(n)]
# 합쳐서 만들 가치의 크기와 동전의 종류를 입력받아 변수에 저장해줍니다.
dp = [0] * (k + 1)
dp[0] = 1
# 최대 가치의 범위만큼의 dp를 만들어주고 가장 작은 가치의 화폐로만 만드는 경우를 0번 인덱스에 1로 넣어줍니다.
for coin in coins:
    # 모든 종류의 동전에 대하여
    for j in range(coin, k + 1):
        if j - coin >= 0:
            dp[j] += dp[j - coin]
            # 동전의 가치만큼 빠진 자리에 저장된 방법만큼 그 동전이 포함된 조합의 경우가 늘어나므로
            # dp[j]에 dp[j - coin] 값을 더해줍니다.

print(dp[-1])
# 마지막 인덱스에 저장된 값을 출력해줍니다.