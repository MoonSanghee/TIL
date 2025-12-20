x1, y1, r1 = map(int, input().split())
x2, y2, r2 = map(int, input().split())
# 주어지는 변수들을 받아줍니다
d = (x2 - x1) ** 2 + (y2 - y1) ** 2
# 두 좌표사이 거리를 구해줍니다
if (r1 + r2) ** 2 > d:
    print('YES')
else:
    print('NO')
# 두 과녁이 만나는지 확인한 결과를 출력해줍니다