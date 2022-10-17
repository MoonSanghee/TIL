n,m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
# 임의의 숫자가 순서에 관계없이 n개 주어지므로 오름차순으로 정렬 해줍니다.
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
# 그리고 n개의 숫자를 인덱스 자리 값을 리스트에 넣어주며 dfs 재귀를 시작하여 리스트에
# m의 길이만큼 숫자가 들어가면 값을 출력해 줍니다.