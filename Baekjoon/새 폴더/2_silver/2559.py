n, l = map(int, input().split())
numbers = list(map(int, input().split()))
result = []
number = 0
for i in range(l):
    number += numbers[i]
result.append(number)
for i in range(n - l):
    result.append(result[i] + numbers[i + l] - numbers[i])
print(result)

# 나의 풀이
n, m = map(int, input().split())
numbers = list(map(int, input().split()))
s = 0
e = m - 1
num = 0
for i in range(s, e + 1):
    num += numbers[i]
nums = [num]
while e < n - 1:
    num -= numbers[s]
    s += 1
    e += 1
    num += numbers[e]
    nums.append(num)
print(max(nums))