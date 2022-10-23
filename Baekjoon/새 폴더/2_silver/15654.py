n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
li = []
check = [0] * n

def dfs(a):
    if a == m:
        return print(*li)
    for i in range(n):
        if not check[i]:
            li.append(nums[i])
            check[i] = 1
            dfs(a + 1)
            check[i] = 0
            li.pop()
dfs(0)