n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
# 주어지는 학생수와 관계수를 받고 관계를 담을 리스트를 만들어줍니다
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
# 친구 관계를 표시해줍니다
for i in range(n):
    print(len(graph[i + 1]))
    # 각 학생별 친구 관계를 출력해줍니다