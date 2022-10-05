n = int(input())
li = []
for i in range(n):
    li.append(i + 1)
nums = list(map(int, input().split()))
for i in range(n):
    moved = i - nums[i]
    for j in range(i, moved, -1):
        li[j], li[j - 1] = li[j - 1], li[j]
print(*li)