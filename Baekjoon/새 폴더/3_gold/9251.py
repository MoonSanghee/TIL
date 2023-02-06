word1 = input()
word2 = input()
# 두 단어를 입력받아줍니다.
dp = [[0]*(len(word2) + 1) for _ in range(len(word1) + 1)]
# 두 단어보다 각각 1씩 큰 가로와 세로 너비를 가지는 영역을 dp로 만들어줍니다.

for i in range(1, len(word1) + 1):
    for j in range(1, len(word2) + 1):
        if word1[i - 1] == word2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            # 순회하는 범위를 1부터 단어의 길이까지 하고있으므로 인덱스값에 맞춰주기위해
            # 1씩 뺀 자리에 위치한 문자가 같다면 두 문자 직전에 위치한 dp[i - 1][j - 1]을
            # 찾아 1을 더한값을 dp[i][j]에 넣어줍니다.
        else:
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
            # 두 문자가 같지 않다면 각 단어에서 한 칸 전의 문자일때 dp값을 찾아 dp[i][j]에 넣어줍니다.

print(dp[-1][-1])
# dp[-1][-1]에 담긴 값을 출력해줍니다.