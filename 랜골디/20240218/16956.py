r, c = map(int, input().split())
maps = [list(input()) for _ in range(r)]
# 주어지는 영역의 크기와 영역의 상태를 받아줍니다.
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
# 4방향 탐색을 설정해줍니다.
for i in range(r):
    for j in range(c):
        if maps[i][j] == 'S':
            # 영역을 순회하며 양이 위치한 자리라면
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if nx in range(r) and ny in range(c):
                    if maps[nx][ny] == '.':
                        maps[nx][ny] = 'D'
                        # 4방향 탐색을 통해 이웃한 영역이 빈 영역일 경우 울타리를 설치하고
                    elif maps[nx][ny] == 'W':
                        print(0)
                        exit()
                        # 늑대가 있다면 0을 출력하고 확인을 멈추어줍니다.

print(1)
for line in maps:
    print(''.join(line))
# 모든 영역을 탐색하였다면 울타리를 설치할 수 있으므로 1을 출력하고
# 각 줄을 string 형태로 바꾸어 출력해줍니다.