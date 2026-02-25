from math import pi

A1, P1 = map(int, input().split())
R1, P2 = map(int, input().split())
# 주어지는 변수들을 받아줍니다
if P1 / A1 < P2 / (R1 ** 2 * pi):
    print("Slice of pizza")
else:
    print("Whole pizza")
# 크기를 비교하여 결과를 출력하여줍니다