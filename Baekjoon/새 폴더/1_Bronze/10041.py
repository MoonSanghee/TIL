w, h, n = map(int, input().split())
spots = [list(map(int, input().split())) for _ in range(n)]
# 주어진 영역의 크기와 방문할 좌표의 개수, 좌표의 정보들을 받아줍니다
result = 0
# 결과를 담을 변수를 설정해줍니다
for i in range(1, n):
    sx, sy = spots[i - 1][0], spots[i - 1][1]
    ex, ey = spots[i][0], spots[i][1]
    # 시작과 도착 좌표를 받아줍니다
    if (ex - sx) * (ey - sy) < 0:
        result += abs(ex - sx) + abs(ey - sy)
    else:
        result += max(abs(ex - sx), abs(ey - sy))
    # 대긱산으로 이동이 가능한지 확인하여 통과해야하는 길의 수를 더해줍니다
print(result)
# 결과를 출력해줍니다