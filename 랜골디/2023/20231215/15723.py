from collections import deque

n = int(input())
# 주어지는 관계의 개수를 받습니다.
premise = dict()
for _ in range(n):
    a, b = input().split(' is ')
    if b in premise:
        premise[b].append(a)
    else:
        premise[b] = [a]
# 각 단어에 도달할 수 있는 출발 단어를 리스트 형태로 만들어줍니다.

m = int(input())
# 확인할 조합이 몇 개인지 받아줍니다.
for _ in range(m):
    a, b = input().split(' is ')
    visited = []
    # 방문처리할 빈 리스트를 만들어 줍니다.
    check = False
    # 확인이 되는지 여부를 불리언 값으로 저장해줍니다.
    if b in premise:
        q = deque()
        q.append(b)
        while q:
            x = q.popleft()
            if x == a:
                check = True
                break
            if x not in visited:
                visited.append(x)
                if x in premise:
                    for i in premise[x]:
                        q.append(i)
    # 도달할 수 있는 방법이 있는지 bfs를 이용해 위로 타고 올라가며 확인해줍니다.
    if check:
        print('T')
    else:
        print('F')
    # 도달하였다면 T, 도달할 수 없다면 F를 출력해줍니다