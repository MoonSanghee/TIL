n, m, k = map(int, input().split())
# 영역의 크기와 선택할 수의 개수를 받아줍니다.
sheet = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
# 수를 받고 방문처리할 2중 리스트를 만들어줍니다.
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
big  = -1e9
# 수의 범위가 음수부터 시작하므로 최대값을 음수로 설정해줍니다.
def check(x, y, idx, result):
    global big
    if idx == k:
        big = max(big, result)
        return
    # 필요한 수를 다 선정했다면 big에 담긴수와 비교하여 갱신해줍니다.
    for i in range(x, n):
        for j in range(y if i == x else 0, m):
            # 범위 안을 순회하며
            if visited[i][j]:
                continue
            # 방문한적 있다면 다음으로 넘어갑니다.
            ok = True
            # 방문 할 수 있는지 bool 형태로 담아줍니다.
            for d in range(4):
                nx = i + dx[d]
                ny = j + dy[d]
                if nx in range(n) and ny in range(m):
                    if visited[nx][ny]:
                        ok = False
            # 4방위로 범위안에 방문한 적 있다면 방문할 수 없다는것을 표시해줍니다.
            if ok:
                visited[i][j] = True
                check(i, j, idx + 1, result + sheet[i][j])
                visited[i][j] = False
            # 방문할 수 있다면 방문처리하고 idx를 1늘리고 자리의 값을 더해준 다음 방문을 취소해줍니다..

check(0, 0, 0, 0)
print(big)
# 0, 0, 0, 0으로 함수를 실행시키고 big에 담긴 값을 출력해줍니다.