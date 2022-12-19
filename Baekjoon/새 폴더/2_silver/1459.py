x, y, w, s = map(int, input().split())

m1 = (x+y) * w
# 평행으로만 이동

if (x + y) % 2 == 0:
# x + y 가 짝수면 대각선으로만 이동
    m2 = max(x, y) * s
else:
# 홀수면 대각선이동 + 평행이동 1번
    m2 = (max(x, y) - 1) * s + w

m3 = (min(x, y) * s) + (abs(x-y) * w)
# 평행이동 + 대각선이동

print(min(m1, m2, m3))
# 3가지 경우중 가장 작은 경우를 출력해줍니다.