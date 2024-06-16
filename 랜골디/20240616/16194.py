n = int(input())
price = [0] + list(map(int, input().split()))
# 카드뭉치의 수와 뭉치별 가격을 받아줍니다.
dp = [1e9] * (n + 1)
dp[0] = 0
# n + 1 크기의 dp 리스트를 만들고 0번 인덱스 값을 0으로 설정해줍니다.
for i in range(n + 1):
    for j in range(i + 1):
        dp[i] = min(dp[i], dp[i - j] + price[j])
# 각 카드 뭉치를 살 경우와 비교하여 dp 값을 갱신해줍니다.
print(dp[-1])
# dp 리스트의 마지막 값을 출력해줍니다.