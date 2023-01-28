from collections import deque
n = int(input())
q = deque()
q.append((1, 0))
# 찾고싶은 자리를 받고 큐에 1번 인덱스에 카피보드엔 빈 값을 넣어줍니다.
visited = dict()
visited[(1, 0)] = 0
# 1만큼의 이모티콘과 카피보드에 0인 값을 가질때는 0의 비용이 필요하다는것을 방문 처리 해줍니다.
while q:
    number, copy = q.popleft()
    if number == n:
        print(visited[(number, copy)])
        # 원하는 자리에 도착하였다면 비용이 얼마나 들었는지 출력해줍니다.
        break
    if (number, number) not in visited:
        visited[(number, number)] = visited[(number, copy)] + 1
        q.append((number, number))
    if (number - 1, copy) not in visited:
        visited[(number - 1, copy)] = visited[(number, copy)] + 1
        q.append((number - 1, copy))
    if (number + copy, copy) not in visited:
        visited[(number + copy, copy)] = visited[number, copy] + 1
        q.append((number + copy, copy))
    # 현재 가지고 있는 카피보드의 이모티콘의 개수를 현재 이모티콘 개수로 갱신하는것과 현재 카피보드를 
    # 유지한 채로 이모티콘을 하나 지우는것 현재 이모티콘에 카피보드의 이모티콘만큼 더해주는 조건을
    # 방문한 적 있는지 확인해주고 새로 방문해주어야하면 큐에 값을 넣어주고 이동 전 거리보다
    # 1만큼 비용이 든다고 확인해줍니다.