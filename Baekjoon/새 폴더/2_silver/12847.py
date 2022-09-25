n, m = map(int, input().split())
nums = list(map(int, input().split()))
s = 0
e = m - 1
mx = 0
for i in range(m):
    mx += nums[i]
num = mx
for i in range(1, n - m + 1):
    num -= nums[s]
    s += 1
    e += 1
    num += nums[e]
    mx = max(mx, num)
print(mx)