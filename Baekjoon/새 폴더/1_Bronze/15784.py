n, a, b = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
# 강의실의 크기와 진서의 위치를 받고 강의실의 정보를 받아줍니다
for i in range(n):
    if maps[a - 1][b - 1] < maps[i][b - 1] or maps[a - 1][b - 1] < maps[a - 1][i]:
        print("ANGRY")
        break
    # 진서가 확인 가능한 자리들을 확인하며 진서보다 잘생긴 사람이 있다면 ANGRY를 출력하고 확인을 멈추어줍니다
else:
    print("HAPPY")
    # 반복이 멈추지 않았다면 진서가 확인 가능한 자리에 진서보다 잘생긴 사람이 없으므로 HAPPY를 출력해줍니다