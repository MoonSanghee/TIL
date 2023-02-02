n, m, c = map(int, input().split())
# 만날 두 학교의 학생수와 성격의 유형을 받아줍니다.
chemi = []
for _ in range(c):
    chemi.append(list(map(int, input().split())))
# chemi라는 리스트에 성격별로 얼마나 만족도를 얻을 수 있는지 넣어줍니다.

dp = [[0]*(m + 1) for _ in range(n + 1)]
# 두 학교의 학생수보다 1씩 큰 너비로 확인값을 저장해줄 리스트를 만들어줍니다.
nl = list(map(int, input().split()))
ml = list(map(int, input().split()))
# nl, ml이라는 리스트로 두 학교 학생들의 성격을 받아줍니다.

for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = max(dp[i - 1][j - 1] + chemi[nl[i - 1] - 1][ml[j - 1] - 1], dp[i][j - 1], dp[i - 1][j])
        # 각 자리의 학생들이 악수를 하려면 두 학생의 이전 학생이 악수를 했어야 합니다.
        # 그렇기 때문에 i번째 학생이 악수를 안 하는 경우와 j번째 학생이 악수를 안 하는 경우
        # i, j자리의 학생이 악수를 하는 세 경우를 비교하여 가장 큰 값을 담아줍니다. 
print(dp[-1][-1])
# 가장 마지막에 담긴 수를 출력해줍니다.