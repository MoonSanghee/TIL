n = int(input())
# 박스의 개수를 받아줍니다.
dp = [0] * 11
dp[2] = 1
# 최대 10개의 박스가 주어지므로 11길이의 dp 리스트를 만들고 인덱스 2에 위치한 값을 1로 갱신해줍니다.
for i in range(3, n + 1):
    middle = i // 2
    dp[i] = (middle) * (i - middle) + dp[middle] + dp[i - middle]
# 박스별 값을 갱신해줍니다.
print(dp[n])
# 찾는 값을 출력해줍니다.