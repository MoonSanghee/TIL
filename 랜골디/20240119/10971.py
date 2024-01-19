n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n
# 방문할 도시의 수와 도시간 방문 비용 방문 여부를 받아줍니다.
result = 10000000
# 결과를 한 개 도시를 방문하는 최대 비용 * 도시의 최대 수인 1000000 * 10으로 설정해줍니다.
def dfs(now, cost, depth):
    global result
    if depth == n:
        if maps[now][0]:
            result = min(result, cost + maps[now][0])
            return
            # 모든 도시를 방문했다면 result값을 비교하여 갱신해줍니다.
    for i in range(1, n):
        if not visited[i] and maps[now][i]:
            visited[i] = True
            dfs(i, cost + maps[now][i], depth + 1)
            visited[i] = False
            # 방문한적 없고 방문 할 수 있다면 재귀를 실행해줍니다.

visited[0] = True
dfs(0, 0, 1)
# 0번 도시를 방문처리하고 0번 도시부터 출발하도록 함수를 실행해줍니다.
print(result)
# result에 담긴 값을 출력해줍니다