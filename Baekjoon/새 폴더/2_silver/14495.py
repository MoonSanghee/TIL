n = int(input())
# 주어지는 변수를 받아줍니다
dp = [1, 1, 1]
for i in range(3, n):
    dp.append(dp[i -1] + dp[i - 3])

print(dp[-1])
# 주어진 방식으로 수열을 만들어 찾는 값을 출력해줍니다