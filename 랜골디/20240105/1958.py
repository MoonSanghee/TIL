x = input()
y = input()
z = input()
# 세개의 단어를 받아줍니다
dp = [[[0] * (len(z) + 1) for _ in range(len(y) + 1)] for _ in range(len(x) + 1)]
# 3단어의 길이 + 1의 크기를 가지도록 3중 리스트를 만들어줍니다.
for i in range(1, len(x) + 1):
    for j in range(1, len(y) + 1):
        for k in range(1, len(z) + 1):
            if x[i - 1] == y[j - 1] and x[i - 1] == z[k - 1]:
                dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1
            else:
                dp[i][j][k] = max(dp[i][j][k - 1], dp[i][j - 1][k], dp[i - 1][j][k])
# 세 단어를 차례로 순회하며 이전까지 연속하는 최장 길이를 확인하고 갱신하여 줍니다.
answer = -1

for i in range(len(x) + 1):
    for j in range(len(y) + 1):
        answer = max(max(dp[i][j]), answer)
# 모든 자리를 확인하여 최장 연속하는 길이를 확인해줍니다.
print(answer)
# 최장 연속하는 길이를 출력해줍니다