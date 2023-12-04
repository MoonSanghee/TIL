n = int(input())
numbers = list(map(int, input().split()))
# 수의 개수와 수열을 받아줍니다.
dp = [0] + [1e9] * (n - 1)
# 각 자리에 도달하는데 필요한 힘을 담기위해 0번 인덱스는 0, 
# 1번부터는 10의 9승을 가지는 n길이의 수열을 만들어줍니다.

for i in range(1, n):
    for j in range(i):
        p = max((i - j) * (abs(numbers[i] - numbers[j]) + 1), dp[j])
        dp[i] = min(dp[i], p)
        # 각 자리를 순회하며 그 이전 자리를 통해 각 자리에 도달하는데 필요한 힘을 구하여 dp[i]에 담아줍니다.

print(dp[-1])
# 마지막 자리에 도달하는데 드는 힘을 출력해줍니다.