n = int(input())
# 사려고하는 카드의 수를 받아줍니다.

costs = [0] + list(map(int, input().split()))
# 0개의 카드를 사는데 0의 비용이 든다는 리스트에 각 카드뭉치를 사는데 드는 비용을 
# 리스트 형태로 받아 더해줍니다.

dp = [0] * (n + 1)
# 각 카드만큼 살 때 가장 큰 비용을 저장할 dp를 만들어줍니다.

for i in range(1, n + 1):
    for j in range(1, i + 1):
        dp[i] = max(dp[i], dp[i - j] + costs[j])
        # 카드를 i장까지 가장 비싸게 사는 방법은 j장만큼을 한번에 사는 방법과 
        # i - j만큼 사는 가장 비싼 값의 합을 비교하여 가장 큰 경우를 찾아주면 됩니다.

print(dp[-1])
# dp리스트의 가장 마지막에 저장된 값을 출력해줍니다.