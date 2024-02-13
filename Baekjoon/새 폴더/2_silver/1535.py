n = int(input())
# 사람의 수를 받아줍니다.
hp = list(map(int, input().split()))
happy = list(map(int, input().split()))
hp, happy = [0] + hp, [0] + happy
# 체력과 행복도를 리스트로 받고 인덱스 자리를 맞춰주기위해 [0] 리스트에 hp와 happy 리스트를 붙여줍니다.
dp = [[0 for _ in range(100)] for _ in range(n + 1)]
# 각 사람별로 체력별 최대 행복도를 저장할 수 있게 2중 리스트를 만들어줍니다.
for i in range(1, n + 1):
    for j in range(1, 100):
        if hp[i] <= j:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - hp[i]] + happy[i])
            # 체력이 충분하다면 악수를 했을때와 안 했을때를 비교하여 dp에 값을 저장해줍니다.
        else:
            dp[i][j] = dp[i - 1][j]
            # 아니라면 직전 체력의 dp값으로 갱신해줍니다.

print(dp[n][99])
# dp의 마지막 행, 마지막 열에 저장된 값을 출력해줍니다.