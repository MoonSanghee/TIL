n, s, m = map(int, input().split())
volumes = list(map(int, input().split()))
# 수의 개수, 시작 볼륨, 최대 볼륨과 조절 가능한 볼륜을 받아줍니다.
dp = [[False] * (m + 1) for _ in range(n + 1)]
# 0부터 m까지 볼륨이 출력될 수 있다고 표시해줄 불리언값 리스트를 n + 1개 가지는 2중 리스트를 만들어줍니다.
dp[0][s] = True
# 시작 볼륨이 출력되는것을 표시해줍니다.
for i in range(n):
    for j in range(m + 1):
        if dp[i][j] == True:
            if j + volumes[i] in range(m + 1):
                dp[i + 1][j + volumes[i]] = True
            if j - volumes[i] in range(m + 1):
                dp[i + 1][j - volumes[i]] = True
            # 출력되는 볼륨을 기준으로 더하거나 뺄 수 있다면 출력될 볼륨을 표시해줍니다.

result = -1
for i in range(m + 1):
    if dp[n][i] == True:
        result = i
# 마지막 단계까지 거친 볼륨중에 출력되는 경우가 있는지 확인하고 가장 큰 값을 찾아 출력해줍니다.
print(result)