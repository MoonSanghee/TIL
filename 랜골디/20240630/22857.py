n, k = map(int, input().split())
s = [0] + list(map(int, input().split()))
# 수열의 길이와 수를 뺄수있는 횟수, 수열을 받아줍니다.
dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
# (n + 1) * (k + 1) 크기의 dp 리스트를 만들어줍니다.
for i in range(1, n + 1):
    s[i] %= 2
    # 홀수인지 짝수인지 여부만 확인하면되므로 s[i] 값들을 2로 나눈 나머지로 갱신해줍니다
    for j in range(k + 1):
        if s[i] == 0:
            dp[i][j] = dp[i - 1][j] + 1
        else:
            if j != 0:
                dp[i][j] = dp[i - 1][j - 1]
        # s[i]가 홀수라면 k인덱스를 하나 옮겨 1개를 뺸 값으로 갱신해주고 짝수라면 빼지않고 값을 갱신해줍니다.

result = 0
for i in dp:
    result = max(result, i[k])
print(result)
# k개까지 빼서 연속하게 만드는 모든 경우를 확인하여 가장 긴 경우를 출력해줍니다.