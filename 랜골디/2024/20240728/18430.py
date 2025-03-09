n, m = map(int, input().split())
# 주어지는 재료의 크기를 받아줍니다.
woods = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
# 재료의 형태를 받고 사용하였는지를 담을 변수를 만들어줍니다.
result = []
d = [(-1, 0, 0, -1), (-1, 0, 0, 1), (1, 0, 0, 1), (1, 0, 0, -1)]
# 결과를 담을 변수를 만들고 부메랑의 4가지 형태를 설정해줍니다.
def com(x, y, total):
    if x == n:
        x = 0
        y += 1
    if y == m:
        result.append(total)
        return
    # x, y를 순회하며 맨 끝에 도착하면 부메랑 강도를 리스트에 담아줍니다.
    if not visited[x][y]:
        # 현재 위치를 부메랑으로 만든적 없다면 
        for dx1, dy1, dx2, dy2 in d:
            nx1, ny1 = x + dx1, y + dy1
            nx2, ny2 = x + dx2, y + dy2
            # 부메랑을 만들 자리를 구하고
            if 0 <= nx1 < n and 0 <= nx2 < n and 0 <= ny1 < m and 0 <= ny2 < m:
                if visited[nx1][ny1] or visited[nx2][ny2]:
                    continue
                # 자리가 영역안에 위치하는지와 사용하였는지를 확인해줍니다.
                else:
                    visited[x][y] = True
                    visited[nx1][ny1] = True
                    visited[nx2][ny2] = True
                    com(x + 1, y, total + woods[x][y] * 2 + woods[nx1][ny1] + woods[nx2][ny2])
                    visited[x][y] = False
                    visited[nx1][ny1] = False
                    visited[nx2][ny2] = False
                # 확인하여 부메랑을 만들수있다면 재귀를 통해 부메랑을 만들고 다음 영역을 확인하도록 재귀하여줍니다.
    com(x + 1, y, total)
    # 부메랑을 만들지 않는 경우를 재귀하여줍니다.

com(0, 0, 0)
print(max(result))
# 0, 0, 0으로 함수를 실행시키고 result 리스트안에 가장 큰 값을 출력해줍니다.