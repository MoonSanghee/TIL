n = int(input())
# 목표액을 받아줍니다
dp = [i for i in range(n + 1)]
# 각 금액은 모두 1원짜리 동전으로 만드는 경우를 리스트에 담아줍니다
for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 1
    
    dp[i] = min(dp[i], dp[i - 2] + 1)
    if i >= 5:
        dp[i] = min(dp[i], dp[i - 5] + 1)
    if i >= 7:
        dp[i] = min(dp[i], dp[i - 7] + 1)
    # 각 금액권의 동전으로 대체하였을때 동전을 덜 쓸수있다면 값을 갱신해줍니다
    
print(dp[-1])
# 결과를 출력해줍니다