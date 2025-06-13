# 크루스칼(Kruskal) 알고리즘

import sys
input = sys.stdin.readline

V, E = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(E)]
graph.sort(key = lambda x : x[2])
# 정점과 간선의 개수를 받고 간선의 정보를 받아 비용의 오름차순으로 정렬해줍니다
Vroot = [i for i in range(V + 1)]
# 각 정점의 부모를 자기 자신으로 설정하여 리스트에 담아줍니다

def find(x):
    if x != Vroot[x]:
        Vroot[x] = find(Vroot[x])
    return Vroot[x]
    # 각 정점의 루트를 찾는 함수를 만들어줍니다

result = 0
# 비용을 담을 변수를 설정해줍니다
for s, e, w in graph:
    sRoot = find(s)
    eRoot = find(e)
    if sRoot != eRoot:
        if sRoot < eRoot:
            Vroot[sRoot] = eRoot
        else:
            Vroot[eRoot] = sRoot
        result += w
    # 간선의 두 정점의 루트를 확인해 다르다면 연결되지 않은 것이므로 연결하고 비용을 추가하여줍니다

print(result)
# 결과를 출력해줍니다