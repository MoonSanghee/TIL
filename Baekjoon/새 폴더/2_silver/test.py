n,m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

li = []
def dfs(a):
    if len(li) == m:
        return print(*li)
    for i in range(a + 1, n):
        li.append(nums[i])
        dfs(i)
        li.pop()
for i in range(n):
    li.append(nums[i])
    dfs(i)
    li.pop()