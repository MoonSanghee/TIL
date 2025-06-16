import heapq
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
# 주어지는 컴퓨터의 수와 연결 할 수 있는 선의 수를 받아줍니다
parents = [i for i in range(N)]
edges = []
for _ in range(M):
    a, b, c = (map(int, input().split()))
    heapq.heappush(edges,(c, a - 1, b - 1))
# 각 컴퓨터의 최상위 부모를 확인하기위한 리스트를 만들고 주어지는 선의 정보를 받아 비용을 가장 앞에 두고 담아줍니다
def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]
# 각 컴퓨터의 최상위 부모 노드를 찾는 함수를 만들어줍니다
def union(a, b):
    a, b = find(a), find(b)
    if a > b:
        a, b = b, a
    parents[b] = a
# 두 노드의 최상위 노드가 같다면 하나의 그룹으로 묶어주는 함수를 만들어줍니다
result = 0
cnt= 0
# 최종 비용과 연결된 선의 개수를 담을 변수를 설정해줍니다
while cnt < N - 1:
    distance, a, b = heapq.heappop(edges)
    if find(a) != find(b):
        union(a, b)
        cnt += 1
        result += distance
    # N - 1개의 선이 연결되면 N개의 컴퓨터를 모두 연결할 수 있습니다
    # 선의 정보를 비용이 적은것부터 받아 최상단에 연결된 부모노드가 다르다면 두 컴퓨터를 연결하고 거리와 선의 개수를 더해줍니다
print(result)
# 최종 비용을 출력해줍니다