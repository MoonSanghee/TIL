from collections import deque
f, s, t, u, d = map(int, input().split())
# 층수, 시작, 목적지, 올라가는 간격, 내려가는 간격을 입력받아 변수에 저장해줍니다.
maps = [-1 for _ in range(f + 1)]
# 엘리베이터를 이용하여 갈 수 있는지 확인하기위해 -1이 층수보다 하나 더 많은 리스트를 만들어줍니다.
def bfs(a):
    q = deque()
    q.append(a)
    maps[a] = 0
    maps[0] = 0
    # 0번 인덱스는 인덱스와 실제 층을 맞춰주기위해 만들어준 자리이기에 0을 넣어 갱신하지 않도록 해주고
    # a의 인덱스는 시작점이니 걸린 시간을 0으로 잡아줍니다.
    while q:
        x = q.popleft()
        for i in [x + u, x - d]:
            if i in range(f + 1) and maps[i] == -1:
            # 올라가는 층과 내려가는 결과가 건물 안에 드는지 확인하고 아직 도착한 적 없다면 값을 갱신해줍니다.
                maps[i] = maps[x] + 1
                q.append(i)

bfs(s)
if maps[t] == -1:
    print('use the stairs')
# 목표 인덱스 값이 -1이면 도달 못하였으므로 계단을 이용하라고 출력해주고
else:
    print(maps[t])
# 목표 인덱스 값이 -1이 아니면 도달하였으므로 걸린 시간을 출력해줍니다.