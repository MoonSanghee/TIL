n = int(input())
nums = list(map(int, input().split()))
total = 0
for i in range(n):
    for j in range(n):
        total += abs(nums[i] - nums[j])
        
print(total)