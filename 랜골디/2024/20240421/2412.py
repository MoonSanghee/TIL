from collections import deque

n, T = map(int, input().split())
# 홈의 개수와 높이를 받아줍니다.
handles = set(tuple(map(int, input().split())) for _ in range(n))
# 홈을 튜플 형식으로 받아 set 구조에 넣어줍니다.
reach = False

q = deque()
q.append((0, 0, 0))
# 덱 자료를 만들고 시작점과 시작점에 도달하는데 필요한 이동을 0으로 설정해 넣어줍니다.
while q:
    x, y, cnt = q.popleft()
    # 덱에서 뺀 값을 좌표와 도달하는데 필요한 이동 비용으로 설정해줍니다.
    if y == T:
        reach = True
        break
    # 정상에 도달한다면 도달하는것을 표시하고 연산을 멈추어줍니다.
    for i in range(-2, 3):
        for j in range(-2, 3):
            nx = x + i
            ny = y + j
            if (nx, ny) in handles:
                q.append((nx, ny, cnt + 1))
                handles.remove((nx, ny))
            # 이동 가능한 범위를 확인하여 홈이 있는지 확인하고 홈이 있다면 이동 횟수를 1증가시킨 값과 좌표를 묶어 덱에 넣고
            # 사용한 흠이므로 set에서는 빼줍니다

if reach:
    print(cnt)
else:
    print(-1)
# 도달하였는지 확인하여 결과값을 출력해줍니다.