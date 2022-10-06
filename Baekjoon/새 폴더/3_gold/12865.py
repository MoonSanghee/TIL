n, k = map(int, input().split())
dp = [0 for _ in range(k + 1)]
items = []
for i in range(n):
    items.append(list(map(int,input().split())))
for item in items:
    w, v = item
    for i in range(k, w - 1, -1):
        # 제한 무게는 k에서 아이템의 무게까지 역순으로 가장 가치있는 조합을 찾아야한다.
        dp[i] = max(dp[i], dp[i - w] + v)
print(dp[-1])
