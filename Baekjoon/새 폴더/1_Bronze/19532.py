a, b, c, d, e, f = map(int, input().split())
# 6개의 수를 받아줍니다.
for x in range(-999, 1000):
    for y in range(-999, 1000):
        if (a * x) + (b * y) == c and (d * x) + (e * y) == f:
            print(x, y)
            break
# 주어진 범위를 순회하며 식이 성랍하는 값을 찾아 출력해줍니다.