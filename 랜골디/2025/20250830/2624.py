t = int(input())
k = int(input())
coins = [list(map(int, input().split())) for _ in range(k)]
# 주어지는 목표 금액과 동전의 개수, 동전의 정보들을 받아줍니다
dp = [0] * (t + 1)
dp[0] = 1
# 동전을 사용하여 각 금액을 만드는 조합의 수를 담을 t+1 길이의 dp리스틀를 만들고 0번 인덱스에 1을 넣어줍니다
for coin, cnt in coins:
    for target in range(t, 0, -1):
        for j in range(cnt):
            if target - (j + 1) * coin >= 0:
                dp[target] += dp[target - coin * (j + 1)]
    # 코인의 정보를 순회하며 금액을 내려오면서 동전들을 사용해 조합을 만들수 있다면 사용해서 만든 경우의 수를 갱신해줍니다
print(dp[-1])
# 목표금액을 만드는 방법의 수를 출력해줍니다