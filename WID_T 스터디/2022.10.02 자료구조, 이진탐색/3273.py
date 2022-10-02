n = int(input())
nums = list(map(int, input().split()))
nums.sort()
x = int(input())
s = 0
e = n - 1
cnt = 0
while s < e:
    for i in range(e, s, -1):
        if nums[s] + nums[i] > x:
            e -= 1
        elif nums[s] + nums[i] == x:
            cnt += 1
            e = i
            break
    s += 1
print(cnt)