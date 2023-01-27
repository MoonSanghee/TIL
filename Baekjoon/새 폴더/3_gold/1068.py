n = int(input())
maps = list(map(int, input().split()))
delete = int(input())
# 노드의 개수와 각 노드의 부모 노드, 지울 노드를 입력받아줍니다.
graph = [[] for _ in range(n)]
for i in range(n):
    if maps[i] != -1:
        if i != delete:
            graph[maps[i]].append(i)
    # 부모가 -1인 경우 관계를 표시할 수 없고 지울 노드일 경우 다시 빼 줄 것이기
    # 때문에 모든 노드를 순서대로 확인하며 두 경우를 제외하고는 부모의 노드에 자식 노드를 표시해줍니다.
def dfs(a):
    while graph[a]:
        x = graph[a].pop()
        dfs(x)
        # 모든 자식 노드를 확인하고 가장 아래 노드부터 연결을 모두 끊은 뒤
    graph[a].append(False)
    # 삭제된 노드임을 표시하기 위해 False를 관계그래프에 넣어줍니다.
dfs(delete)
# 삭제할 노드를 기준으로 함수를 가동시켜줍니다.
cnt = 0
for i in range(n):
    if not graph[i]:
        cnt += 1
        # 모든 노드를 순회하며 자식 노드가 없는 경우를 확인하여줍니다.

print(cnt)
# 확인한 자식 노드가 없는 노드의 개수를 출력하여 줍니다.