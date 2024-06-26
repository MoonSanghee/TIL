# 타일이 하나일 경우 1
# 타일이 2개일 경우 00, 11
# 타일이 3개일 경우 100, 001, 111
# 타일이 4개일 경우 1100, 1001, 1111, 0000, 0011
# 이처럼 나열해보면 2보다큰 n개의 타일로 만들 수 있는 타일의 형태는 1타일 1개와 n-1개의 타일로
# 만들어지는 조합과 00타일에 n - 2개의 타일로 만드는 조합들을 합친 형태가 됩니다.
dp = [1, 2]
# 따라서 dp에 1개의 타일과 2개의 타일로 만들수 있는 조합을 인덱스에 넣어주고
n = int(input())
for i in range(2, n):
    dp.append((dp[i - 1] + dp[i - 2])%15746)
    # n-1개의 인덱스가 될 때까지 i-1, i-2의 합을 15746으로 나눈값을 넣어준다음
print(dp[n-1])
# dp[n-1]의 위치에 있는 값을 출력합니다.