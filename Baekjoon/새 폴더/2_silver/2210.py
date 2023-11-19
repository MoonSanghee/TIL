sheet = [list(map(str, input().split())) for _ in range(5)]
# 5 * 5 사이즈의 2중 리스트를 받아줍니다.
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
# 이동할 4방향을 설정해줍니다.
com = []
result = []
# 6자리 조합을 만들 리스트와 만들어진 조합을 담을 리스트를 만들어줍니다.

def bfs(x, y):
    if len(com) == 6:
        result.append(''.join(com))
        # 조합의 길이가 6자리라면 문자열로 만들어 result에 담아줍니다.
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx in range(5) and ny in range(5):
                com.append(sheet[nx][ny])
                bfs(nx, ny)
                com.pop()
                # 4방향탐색이 가능하다면 시행하여 값을 추가한다음 이동한 좌표로
                # 함수를 다시 실행하여줍니다.

for i in range(5):
    for j in range(5):
        bfs(i, j)
        # 2중 리스트의 모든 좌표에서 함수를 실행시켜줍니다.

print(len(set(result)))
# result값을 set 형태로 변환시켜 중복을 거른 결과를 출력하여줍니다.