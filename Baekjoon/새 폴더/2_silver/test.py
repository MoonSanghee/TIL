n = int(input())
li = list(map(int, input().split()))
dp = [1 for _ in range(n)]

for i in range(1, n):
    s = []
    for j in range(i):
        if li[i] < li[j]:
            s.append(dp[j])
    if s:
        dp[i] += max(s)
    else:
        continue
print(max(dp))