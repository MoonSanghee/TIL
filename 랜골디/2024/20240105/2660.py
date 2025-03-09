from collections import deque

n = int(input())

friends = [[] for _ in range(n + 1)]
points = [0] * (n + 1)
result = [[50, 0], []]
# 친구 관계, 점수, 결과를 담을 리스트를 만들어줍니다.
a, b = map(int, input().split())

while True:
    if a == b and a == -1:
        break
    # -1, -1을 입력받을때까지 관계를 받아줍니다.
    friends[a].append(b)
    friends[b].append(a)
    a, b = map(int, input().split())
    # 친구 관계를 양방향 관계로 추가시켜줍니다.

for i in range(1, n + 1):
    visited = [0] * (n + 1)
    def bfs(s):
        visited[s] = 1
        q = deque()
        q.append(s)
        while q:
            x = q.popleft()
            for i in friends[x]:
                if visited[i] == 0:
                    q.append(i)
                    visited[i] = visited[x] + 1
        # 본인 자리부터 몇 점으로 모든 사람을 알게되는지 확인해주는 함수입니다.
    bfs(i)
    # 함수를 실행하여 모든 사람을 알기위해 필요한 점수를 구해줍니다.
    if max(visited) - 1 < result[0][0]:
        result[0][0] = max(visited) - 1
        result[0][1] = 1
        result[1] = [i]
        # 최저점을 갱신하였다면 점수와 최저점자, 최저점자 목록을 갱신해줍니다.
    elif max(visited) - 1 == result[0][0]:
        result[0][1] += 1
        result[1].append(i)
        # 최저점이 동률이라면 최저점자와 목록을 추가해줍니다.

print(*result[0])
print(*result[1])
# 최저점과 최저점자의 수, 최저점자의 목록을 차례로 출력해줍니다.