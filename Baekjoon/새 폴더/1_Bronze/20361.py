n, x, k = map(int, input().split())
# 주어지는 변수들을 받아줍니다
for _ in range(k):
    a, b = map(int, input().split())
    if x == a:
        x = b
    elif x == b:
        x = a
# 교환하는 컵에 공이 있다면 공의 위치를 변경해줍니다
print(x)
# 결과를 출력해줍니다