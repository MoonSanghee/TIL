from collections import deque

n = int(input())
nums = list(map(int, input().split()))
# 수의 개수와 나열을 받아줍니다.

dp = [n + 1 for _ in range(n)]
dp[0] = 0
# 점프 회수를 확인할 수의 개수와 같은 크기의 dp 리스트를 만들어주고 
# dp[0]은 0으로 나머지는 각 값으로 n + 1을 넣어줍니다.

for i in range(n):
    for j in range(1, 1 + nums[i]):
        if i + j < n:
            dp[i + j] = min(dp[i + j], dp[i] + 1)
# 각 자리에서 점프 가능한 거리만큼을 확인하며 dp[i + j]에 저장된 값과
# dp[i]에서 점프하여 도달하는 점프수를 비교하여 적은것을 넣어줍니다.

if dp[n - 1] == n + 1:
    print(-1)
else:
    print(dp[n - 1])
# 마지막 값이 변하지 않았다면 도달하지 못한것이므로 -1을 출력해주고 바뀌었다면
# 점프 횟수를 출력해줍니다.