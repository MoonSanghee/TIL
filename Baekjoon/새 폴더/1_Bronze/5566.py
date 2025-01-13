n, m = map(int, input().split())
board = [int(input()) for _ in range(n)]
dice = [int(input()) for _ in range(m)]
# 보드의 각 자리에 도달하였을때 이동과 주사위 눈의 결과를 차례로 받아줍니다
p = 0
# 현재 위치를 담을 변수를 설정해줍니다
for i in range(m):
    p += dice[i]
    if p >= n - 1:
        print(i + 1)
        break
    # 주사위의 눈만큼 이동하고 마지막 칸에 도달하면 멈추어줍니다
    p += board[p]
    if p >= n - 1:
        print(i + 1)
        break
    # 도착한 칸의 명령만큼 추가로 움직이고 마지막 칸 이상에 도달한다면 멈추어줍니다