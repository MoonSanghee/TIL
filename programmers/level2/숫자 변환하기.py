from collections import deque
def solution(x, y, n):
    answer = 0
    dp = [0 for _ in range(1000001)]
    # 범위 안을 확인하기위해 주어진 범위 크기의 리스트를 만들어줍니다.
    dp[x] = 1
    # x의 위치를 1로 만들어줍니다.

    q = deque()
    q.append((x, 1))
    # q에 x와 비용을 튜플로 묶어 넣어줍니다.
    while q:
        num, cnt = q.popleft()
        # q에서 가장 앞의 값을 확인해서 num과 cnt로 이름 붙여줍니다.
        if num == y:
            break
        # q에서 뺀 num이 y라면 원하는 값에 도착하였으므로 확인을 멈추어줍니다.
        if num + n <= 1000000 and dp[num + n] == 0:
            dp[num + n] = dp[num] + 1
            q.append((num + n, cnt + 1))
        if num * 2 <= 1000000 and dp[num * 2] == 0:
            dp[num * 2] = dp[num] + 1
            q.append((num * 2, cnt + 1))
        if num * 3 <= 1000000 and dp[num * 3] == 0:
            dp[num * 3] = dp[num] + 1
            q.append((num * 3, cnt + 1))
        # 주어진 세 조건으로 연산하여 범위안에 있고 방문한 적 없는지 확인해줍니다.
    if dp[y]:
        answer = dp[y] - 1
        # y에 도달하였다면 x에 도달하는 비용을 1로 시작하였기 때문에 y에 위치한 값에서
        # 1을 뺀 값을 출력해주고
    else:
        answer = -1
        # 도달하지 못하였다면 -1로 만들어 도달하지 못했음을 표시해줍니다.
    return answer
    # 결과를 출력해줍니다.