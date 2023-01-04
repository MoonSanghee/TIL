from collections import deque

n, k = map(int, input().split())
# 출발점과 목표 지점을 변수에 저장해줍니다.
dp = [-1] * 100001
dp[n] = 0
# 이동가능한 범위의 크기만큼의 -1를 가지는 리스트틑 만들어줍니다, 
q = deque()
q.append(n)
# 덱에 n을 넣어줍니다.

while q:
    x = q.popleft()
    if x == k:
        print(dp[k])
        break
    # q에서 출력되는 값이 k일때 dp[k]를 출력하고 반복문을 멈추어줍니다.
    if 2 * x in range(100001) and dp[x * 2] == -1:
        dp[2* x] = dp[x]
        q.append(2 * x)
        # 순간이동 가능한 위치에 방문한적이 없다면 시간이 안 걸리고 방문 표시를 해줍니다.
    if x - 1 in range(100001) and dp[x - 1] == -1:
        dp[x - 1] = dp[x] + 1
        q.append(x - 1)
    if x + 1 in range(100001) and dp[x + 1] == -1:
        dp[x + 1] = dp[x] + 1
        q.append(x + 1)
    # 전후 1칸거리에 방문한 적 없다면 시간을 1만큼 사용하여 이동해줍니다.