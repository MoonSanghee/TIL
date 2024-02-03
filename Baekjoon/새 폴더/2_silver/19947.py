base, y = map(int, input().split())
# 기본금과 저축할 기간을 받아줍니다.
dp = [0] * (y + 1)
dp[0] = base
# 확인할 연수 + 1년의 길이의 리스트를 만들고 0번 인덱스에 기본금을 값으로 설정해줍니다.
for i in range(1, y + 1):
    if i >= 5:
        dp[i] = max(dp[i - 1] * 1.05, dp[i - 3] * 1.2, dp[i - 5] * 1.35)
    elif i >= 3:
        dp[i] = max(dp[i - 1] * 1.05, dp[i - 3] * 1.2)
    else:
        dp[i] = dp[i - 1] * 1.05
    dp[i] = int(dp[i])
    # 5년 혹은 3년 이상일 경우 3, 5년의 이율을 적용받는것에 비해 어떤 경우가 결과가 큰지 확인해정수로 값을 저장합니다.

print(dp[y])
# 결과값을 출력해줍니다.