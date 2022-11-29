import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)
# 깊이 우선 탐색이기에 재귀의 깊이를 넉넉하게 만들어주었습니다.
n, m, s = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
# 입력받는 양방향 그래프를 표시해주었습니다
result = [0] * (n + 1)
cnt = 1
result[s] = cnt
# 도착 결과를 저장해줄 리스트를 만들고 방문 순서를 확인할 변수를 지정후 시작점을 방문표시 해주었습니다.
def dfs(x):
    global cnt
    graph[x].sort()
    for i in graph[x]:
        if result[i] == 0:
            cnt += 1
            result[i] = cnt
            dfs(i)
            # 재귀를 통해 방문한 적 없는 인덱스라면 방문 표시를 해주고 global에 위치한 cnt 값을 1씩 증가시켜주었습니다.

dfs(s)

for i in range(1, n + 1):
    print(result[i])
    # 1번 자리부터 차례로 도착하는데 얼마나 걸렸는지 출력해 주었습니다.