from collections import deque

n, k = map(int, input().split())
visited = dict()
# 출발 위치와 목적지를 받고 방문처리를 해줄 딕셔너리를 만들어줍니다.
def bfs(now):
    q = deque()
    q.append(now)
    # deque 형태의 q에 시작위치를 입력받아줍니다.
    while q:
        # q에 값이 있으면 계속 이동하고
        x = q.popleft()
        if x == k:
            return
            # 도착한 위치가 목적지라면 되돌려줍니다.
        for i in [x - 1, x + 1, 2 * x]:
            if i in range(100001):
                if i not in visited:
                    # 이동 가능한 3곳의 위치가 제한범위 안이고 방문한 적이 없으면
                    visited[i] = x
                    q.append(i)
                    # 어디에서 출발하여 도착했는지 입력해주고 q에 도착한 위치를 넣어줍니다.

bfs(n)
# 함수를 작동시켜줍니다.
result = [k]
while k!=n:
    k = visited[k]
    result.append(k)
print(len(result) - 1)
# 목적지부터 어디에서 이동하여 도착하였는지 역으로 확인하며 순서에 따라 리스트에 담아줍니다.
# 출발위치에서는 시간을 사용하지 않기때문에 길이에서 1을 뺀값을 출력합니다..
print(*result[::-1])
# 목적지부터 역으로 이동한 경로가 담겨있으니 뒤집어서 출력을 해줍니다.