n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
result = []

def dfs(a):
    if len(result) == m:
        print(*result)
        return
    for i in range(a, n):
        result.append(nums[i])
        dfs(i)
        result.pop()
# dfs를 통해 재귀를 돌려주지만 시작하는 위치 값을 보내주어 그 값 이후의 값만 순회하도록
# 하여 범위를 조정하였습니다.
dfs(0)
