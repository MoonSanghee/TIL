T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    board = [input() for _ in range(n)]
    # 주어지는 영역의 크기를 받고 영역의 상태를 받아줍니다
    flag = False
    # 오목이 완성되는지 확인할 변수를 설정해줍니다
    dx = [1, 0, 1, -1]
    dy = [0, 1, 1, 1]
    # 가로, 세로와 두 방향의 대각선을 받아줍니다
    for x in range(n):
        for y in range(n):
            if board[x][y] == 'o':
                # 모든 영역을 순회하며 바둑돌이 놓인 자리를 찾아줍니다
                for i in range(4):
                    nx = x
                    ny = y
                    for j in range(4):
                        nx += dx[i]
                        ny += dy[i]
                        if nx not in range(n) or ny not in range(n) or board[nx][ny] != 'o':
                            break
                    else:
                        flag = True
                    # 4방향을 탐색하며 오목이 완성되는 자리가 있는지 확인해줍니다
    
    if flag:
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')
    # 결과를 출력해줍니다