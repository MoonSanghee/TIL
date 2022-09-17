from itertools import combinations
n, t = map(int, input().split())
numbers = list(map(int, input().split()))

cnt = 0
for i in range(1, n + 1):
    a = combinations(numbers, i)
    for j in a:
        if sum(j) == t:
            cnt += 1
print(cnt)

# dfs 이용
def dfs(idx, result):
    global cnt
    if idx >= n:
        return
    sum += s_[idx]
    if result == s:
        cnt += 1
    dfs(idx + 1, result - s_[idx])
    dfs(idx + 1, result)
n, s = map(int, input().split())
s_ = list(map(int, input().split()))
cnt = 0
dfs(0, 0)
print(cnt)