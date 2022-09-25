# n = int(input())
# nums = [0] * 10001
# for i in range(n):
#     num = int(input())
#     nums[num] += 1
# for i in range(10001):
#     for j in range(nums[i]):
#         print(i)
n = int(input())
seet = []
for i in range(n):
    each = list(map(int, input().split()))
    seet.append(each)
seet.sort(key = lambda x : (x[0], x[1]))
print(seet)