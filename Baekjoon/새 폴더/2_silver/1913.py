n = int(input())
t = int(input())
# 영역의 크기와 타겟수를 설정해줍니다.
maps = [[0]*n for _ in range(n)]
num = n*n
# 영역을 설정해주고 n의 제곱을 시작수로 잡아줍니다.
v = 0
x, y = 0, 0
# 이동 방향과 현재 위치를 설정해줍니다.
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
# 하우상좌 순으로 이동 방향을 설정해줍니다.
tp = [0, 0]
# 타겟의 위치를 저장해줄 변수를 설정해줍니다.
while num >= 1:
    maps[x][y] = num
    # 현재 위치 값을 갱신해줍니다.
    if num == t:
        tp = [x + 1, y + 1]
        # 값이 타겟수라면 타겟의 위치를 저장해줍니다.
    nx = x + dx[v]
    ny = y + dy[v]
    # 현재 위치에서 이동 방향으로 이동을 적용한 값을 구해줍니다.
    if nx not in range(n) or ny not in range(n) or maps[nx][ny]:
        # nx나 ny가 영역을 벗어났거나 이미 값이 저장되어있다면
        v += 1
        v %= 4
        # 이동 방향을 바꾸어주고
        nx = x + dx[v]
        ny = y + dy[v]
        # nx, ny의 값을 변경시켜줍니다.
    x, y = nx, ny
    # x, y를 nx, ny로 갱신해주고
    num -= 1
    # 저장할 값을 1줄여줍니다.
for i in maps:
    print(*i)
# 2중 리스트의 각 리스트안에 들어있는 값들을 출력해주고 
print(*tp)
# 타겟의 위치를 출력해줍니다.