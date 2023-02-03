word1 = input()
word2 = input()
dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
# 두 문자보다 1씩 큰 가로 세로의 크기를 가지는 영역의 리스트를 만들어줍니다.
result = 0
for i in range(1, len(word1) + 1):
    for j in range(1, len(word2) + 1):
        # 단어의 모든 문자를 순회하며
        if word1[i - 1] == word2[j - 1]:
            # 두 문자가 같다면 앞자리 문자도 연속했는지 확인해줍니다.
            dp[i][j] = dp[i - 1][j - 1] + 1
            # 연속하다면 앞자리 문자보다 1만큼 더 길게 이어진다고 표시해줍니다.
            result = max(result, dp[i][j])
            # 최대 길이를 갱신해줍니다.
print(result)
# 최대 길이를 출력해줍니다.