from copy import deepcopy

maps = []
result = 0
# 생선의 위치와 방향을 담을 변수와 상어가 먹은 생선의 점수 최대값을 담을 변수를 설정합니다.
for i in range(4):
    state = list(map(int, input().split()))
    line = []
    for j in range(4):
        line.append([state[j * 2], state[j * 2 + 1] - 1])
    maps.append(line)
    # 생선의 번호와 방향을 묶어 리스트로 각줄을 고쳐준다음 영역에 넣어줍니다.

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]
# 주어지는 이동 8방향을 차례대로 설정해줍니다.

def dfs(sx, sy, score, maps):
    global result
    # 글로벌에 위치한 결과와 비교해줍니다.
    score += maps[sx][sy][0]
    maps[sx][sy][0] = 0
    result = max(result, score)
    # 시작 좌표의 생선을 먹고 점수를 갱신한 다음 글로벌 결과를 갱신해줍니다.

    for i in range(1, 17):
        # 모든 생선이 번호순으로 움직이므로
        fx, fy = -1, -1
        for x in range(4):
            for y in range(4):
                if maps[x][y][0] == i:
                    fx, fy = x, y
                    break
        # 영역을 순회하며 생선을 차례대로 찾아줍니다.
        
        if fx == -1 and fy == -1:
            continue
        # fx와 fy가 갱신되지 않았다면 잡아먹힌것이므로 다음 생선을 확인해줍니다.

        fd = maps[fx][fy][1]
        # 생선의 이동 방향을 담아줍니다.

        for j in range(8):
            nd = (fd + j) % 8
            nx = fx + dx[nd]
            ny = fy + dy[nd]
            if 0 <= nx < 4 and 0 <= ny < 4:
                if not (nx == sx and ny == sy):
                    maps[fx][fy][1] = nd
                    maps[fx][fy], maps[nx][ny] = maps[nx][ny], maps[fx][fy]
                    break
                # 생선을 담겨있는 방향부터 반시계 방향으로 회전하며 돌수있는 방향을 찾고 
                # 이동 가능하다면 이동할 위치의 생선과 위치를 바꾸어줍니다.
        
    sd = maps[sx][sy][1]
    # 상어의 이동 방향을 받아줍니다.
    for i in range(1, 5):
        nx = sx + dx[sd] * i
        ny = sy + dy[sd] * i
        if 0 <= nx < 4 and 0 <= ny < 4 and maps[nx][ny][0] > 0:
            dfs(nx, ny, score, deepcopy(maps))
            # 이동 방향의 칸들을 순회하며 영역을 벗어나지않고 생선이있다면 재귀하여줍니다.

dfs(0, 0, 0, maps)
print(result)
# 함수를 실행시키고 결과를 출력해줍니다.