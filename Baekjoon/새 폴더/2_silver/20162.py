# 나의 풀이
n = int(input())
maps = []
for i in range(n):
    maps.append(int(input()))
dp = [0 for _ in range(n)]
for i in range(n):
    for j in range(i):
        if maps[i] > maps[j]:
            if dp[j] > dp[i]:
                dp[i] = dp[j]
    dp[i] += maps[i]
print(dp)


# 찾아본 풀이
n = int(input())
snack = int(input())
dp = [snack]
dp2 = [snack]

for i in range(n - 1):
    snack = int(input())

    tmp = []
    for i in range(len(dp)):
        i, v = i, dp[i]
        if v < snack:
            tmp.append(dp2[i])
        dp.append(snack)
        if tmp:
            dp2.append(max(tmp) + snack)
        else:
            dp2.append(snack)
print(max(dp2))


# 찾아본 풀이 2
n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))

dp = [0 for _ in range(n)]
dp[0] = numbers[0]
for i in range(1, n):
    dp[i] = numbers[i]
    for j in range(i - 1, -1, -1):
        if numbers[i] > numbers[j]:
            dp[i] = max(dp[i], dp[j] + numbers[i])

print(max(dp))