from collections import deque

n ,m = map(int, input().split())

ladders = [list(map(int, input().split())) for _ in range(n)]
ladders.sort(key=lambda x : x[0])
snakes = [list(map(int, input().split())) for _ in range(m)]
snakes.sort(key=lambda x : x[0])
# 각각 입력받은 사다리와 뱀을 2중 리스트 형태로 담아줍니다.
visited = [0] * 101
# 방문한적이 있는지 표시해줄 리스트를 만들어줍니다.
def bfs(a, b):
    q = deque()
    q.append([a, b])
    while q:
        x, y = q.popleft()
        if x == 100:
            break
        # 100에 도착하였을때 멈추어줍니다.
        for i in range(1, 7):
            nx = x + i
            ny = y + 1
            # 주사위는 1~6까지의 눈을 가지니 1부터 6까지 순회하며 자리를 이동할 경우 주사위를 굴린 횟수를 더해줍니다.
            for j, k in ladders:
                if j == nx:
                    nx = k
            for j, k in snakes:
                if j == nx:
                    nx = k
            # 도착한 값이 사다리 혹은 뱀이 위치한 자리인지 확인해주고
            if nx <= 100:
                if visited[nx] > ny or not visited[nx]:
                    # 도착한 자리가 게임판 안인지와 방문한 적이 있는지 더 적은 횟수의 이동으로 도착할 수 있는지 확인해줍니다.
                    visited[nx] = ny
                    # 최소한으로 이동하여 도착할 때의 이동횟수를 표시해주고
                    q.append([nx, ny])
                    # 위치와 이동횟수를 리스트로 q에 넣어줍니다.
    return y
    # 반복이 멈추었을때 y(이동횟수)를 반환합니다.

print(bfs(1, 0))
# 시작 위치는 1번이고 아직 주사위를 굴리지 않은 상태이니 1, 0을 bfs에 넣고 반환한 값을 출력해줍니다.

# 방문한 자리에 계속 다시 방문하는것을 해결하지 않아서 여러번 틀렸음.