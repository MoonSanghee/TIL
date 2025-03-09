n = int(input())
coins = []
# 목표하는 금액을 받고 금액 이하의 모든 화폐를 담을 변수를 설정해줍니다
for i in range(2, n + 1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        coins.append(i)
# n이하의 모든 소수를 찾아 화폐에 담아줍니다
dp = [0] * (n + 1)
dp[0] = 1
# 가지수를 담을 dp리스트를 만들고 0번 인덱스에 1을 담아줍니다
for i in coins:
    for j in range(i, n + 1):
        dp[j] = (dp[j] + dp[j - i]) % 123456789
# n이하의 값들을 만드는 경우의 수를 누적하여 123456789로 나눈 값을 갱신해줍니다
print(dp[n])
# dp[n]에 담긴 값을 출력해줍니다