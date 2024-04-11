n = int(input())
numbers = list(map(int, input().split()))
# 주어지는 수의 개수와 수열을 받아줍니다.
dp = numbers[::]
# numbers와 같은 값을 가지는 dp를 만들어줍니다.
for i in range(n):
    for j in range(i):
        if numbers[j] > numbers[i]:
            dp[i] = max(dp[i], dp[j] + numbers[i])
# 각 자리까지 순회하며 감소할 수 있다면 그 자리의 값을 더한 경우와 안 더한 경우를 비교하여 큰 값으로 값을 갱신해줍니다.
print(max(dp))
# 가장 값이 큰 경우를 찾아 출력해줍니다.
