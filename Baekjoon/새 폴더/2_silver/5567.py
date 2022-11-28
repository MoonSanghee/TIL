n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    # 양방향 관계를 표현해 줍니다.
check = [0] * (n + 1)
# 초대를 보낼 사람을 표시할 리스트를 만들어줍니다.
li = []
for i in graph[1]:
    check[i] = 1
    li += graph[i]
    # 친구를 초대했으면 초대할 수 있는 그 친구의 친구를 리스트에 담습니다.

for i in li:
    check[i] = 1
    # 친구의 친구를 초대하고
check[1] = 0
# 상근이가 포함되었을수 있으니 상근이는 초대하지 않는다고 바꾸어줍니다.
print(sum(check))
# 초대를 받을 사람을 다 더하여줍니다.