n = int(input())
graph = [[] for _ in range(n + 1)]
islands = [0 for _ in range(n + 1)]
# 섬의 개수와 섬에 있는 늑대 혹은 양을 담을 리스트 섬의 연결을 표시할 리스트를 만들어줍니다.
for i in range(2, n + 1):
    t, a, p = list(input().split())
    if t == 'S':
        islands[i] = int(a)
    else:
        islands[i] = - int(a)
    graph[int(p)].append(i)
# 섬에 있는것이 양이라면 양수를 늑대라면 음수를 담고 연결된것을 표시해줍니다.

def move(idx):
    result = 0
    for i in graph[idx]:
        result += move(i)
    # 각 섬에서 연결된 섬을 확인하여 양이 몇마리 넘어오는 양을 더해줍니다.
    result += islands[idx]
    if result < 0:
        result = 0
    return result
    # 양이 음수만큼 도달하였다면 0으로 바꾸어주고 도착한 양을 return해줍니다.

print(move(1))
# 1번섬에서 함수를 실행시킨 결과를 출력해줍니다.