# 1.
n = int(input())
d = [0 for _ in range(n + 1)]

for i in range(2, n + 1):
    d[i] = d[i - 1] + 1
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
print(d[n])

# 2.
from collections import deque

dp = [10**6] * (10**6 + 1)
# 최대 입력값이 10**6이기때문에 10**6을 인덱스 값으로 10**6 + 1개 가지는 리스트를
# dp로 만들어줍니다.
n = int(input())
dp[n] = 0
# 시작할 숫자를 받아주고 리스트의 시작 인덱스 값을 0으로 만들어줍니다.
q = deque()
q.append((n, 0))
# 덱 자료형에 (n, 0)이라는 값을 넣어줍니다.
while q:
    x, cost = q.popleft()
    # 덱의 왼쪽에서 뺀 값을 현재 위치 x와 연산 횟수인 cost로 받아줍니다.
    if x == 1:
        print(cost)
        break
    # x가 1에 도착하였다면 몇번의 연산이 사용되었는지 출력해주고 작동을 멈추어줍니다.
    if dp[x - 1] > dp[x] + 1:
        dp[x - 1] = dp[x] + 1
        q.append((x - 1, cost + 1))
        # dp[x - 1]을 방문하는것이 최소 연산 횟수를 갱신할 수 있다면 방문하고 
        # 좌표, 연산횟수를 튜플로 묶어 q에 넣어줍니다.
    if not x % 2:
        dp[x // 2] = dp[x] + 1
        q.append((x // 2, cost + 1))
        # 2로 나누어 떨어지는지 확인하고 나누어지면 방문하여 연산 횟수를 갱신하고
        #  좌표, 연산횟수를 튜플로 묶어 q에 넣어줍니다.
    if not x % 3:
        dp[x // 3] = dp[x] + 1
        q.append((x // 3, cost + 1))
        # 3로 나누어 떨어지는지 확인하고 나누어지면 방문하여 연산 횟수를 갱신하고 
        # 좌표, 연산횟수를 튜플로 묶어 q에 넣어줍니다.