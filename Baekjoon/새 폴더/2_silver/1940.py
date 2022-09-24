n = int(input())
m = int(input())
nums = list(map(int, input().split()))
nums.sort()
s = 0
e = n - 1
cnt = 0
while s < e:
    num = nums[s] + nums[e]
    if num > m:
        e -= 1
    elif num < m:
        s += 1
    else:
        cnt += 1
        s += 1
        e -= 1
print(cnt)