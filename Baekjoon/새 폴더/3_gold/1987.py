r, c = map(int, input().split())
seet = [list(input()) for _ in range(r)]
# 주어지는 입력의 크기를 받고 입력을 받아줍니다.
result = 0
alpha = set()
alpha.add(seet[0][0])
# 최장 길이를 담을 변수를 설정하고 사용한 알파벳을 담을 세트를 만든뒤 시작점을 넣어줍니다.
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
# 4방향 탐색을 설정해줍니다.
def dfs(x, y, z):
    global result
    result = max(result, z)
    # 함수가 실행될때 최장길이를 확인하고 갱신해줍니다
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx in range(r) and ny in range(c) and seet[nx][ny] not in alpha:
            alpha.add(seet[nx][ny])
            dfs(nx, ny, z + 1)
            alpha.remove(seet[nx][ny])
        # 4방향 탐색을 통해 사용하지 않은 칸이라면 방문해줍니다. 
    return

dfs(0, 0, 1)
print(result)
# 함수를 실행하고 결과를 출력해줍니다.