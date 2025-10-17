a, b, c = map(int, input().split())
# 주어지는 변수들을 받아줍니다
a, b = abs(a), abs(b)
# 원점에서 떨어진 거리만 필요하므로 주어진 좌표 값을 절대값으로 바꾸어줍니다
if c >= (a + b) and c % 2 == (a + b) % 2:
    print("YES")
else:
    print("NO")
# 판별 결과를 출력해줍니다