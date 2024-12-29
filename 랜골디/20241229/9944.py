case = 1
result = 1000001
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
# 테스트 케이스의 번호와 결과를 담을 변수, 4방향을 설정해줍니다
def check():
    for i in range(n):
        if '.' in maps[i]:
            return False
    return True
# 방문 가능한 자리가 남아있다면 유효하지 않고 없다면 모두 방문하였음을 확인해주는 함수입니다.abs

def move(x, y, cnt):
    global result
    if check():
        result = min(result, cnt)
    # 모두 방문하였는지 확인하여 모두 방문하였다면 결과값을 갱신해줍니다
    if cnt < result:
        # 이동한 횟수가 결과에 담긴 횟수보다 많아지면 더이상 확인할 필요가 없으므로 적은 경우만 확인해줍니다ㄴ
        for i in range(4):
            # 4방향을 돌아가며 이동 가능한지 확인하여 이동하면 재귀하여줍니다
            arr = []
            # 이동이 가능하다면 그 방향으로 이동하며 지나는 지점을 모두 담을 리스트를 만들어줍니다
            nx = x
            ny = y
            while True:
                nx += dx[i]
                ny += dy[i]
                if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == '.':
                    arr.append((nx, ny))
                    maps[nx][ny] = '*'
                else:
                    break
            # 영역을 벗어나거나 이동이 안 되는 칸에 도달할때까지 이동해줍니다
            if arr:
                move(nx - dx[i], ny - dy[i], cnt + 1)
            # 이동을 실행하였다면 마지막 좌표에서 한 칸 돌아간 좌표에서 재귀해줍니다
            for nx, ny in arr:
                maps[nx][ny] = '.'
            # 이동한 좌표들을 다시 방문하지 않았다고 표시해줍니다

while True:
    try:
        n, m = map(int, input().split())
        maps = list(list(input()) for _ in range(n))
        # 영역의 크기와 상태를 받아줍니다
        result = 10000001
        # 결과값을 받을 변수를 세팅해줍니다
        for i in range(n):
            for j in range(m):
                if maps[i][j] == '.':
                    maps[i][j] = '*'
                    move(i, j, 0)
                    maps[i][j] = '.'
                    # 영역을 순회하며 이동 가능한 좌표라면 방문처리를 하고 함수를 실행시켜 결과값이 갱신되는지 확인해줍니다
        if result > 1000000:
            result = -1
        # 결과값이 갱신된적 없다면 모든 빈 칸을 방문할 수 없으므로 -1을 결과값으로 수정해줍니다
        
        print(f"Case {case}: {result}")
        case += 1
        # 주어진 양식에 맞게 결과를 출력해줍니다
    except:
        break
    # 입력이 없다면 멈추어줍니다