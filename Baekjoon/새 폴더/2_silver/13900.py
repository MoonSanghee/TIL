n = int(input())
nums = list(map(int, input().split()))
sum_ = sum(nums)
result = 0
for num in nums:
    sum_ -= num
    result += num * sum_
print(result)