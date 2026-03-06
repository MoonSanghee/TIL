A, B = map(int, input().split())
# 주어지는 두 정수를 받아줍니다
for x in range(-1000, 1001):
    if x ** 2 + 2 * A * x + B == 0:
        print(x, end = ' ')
        # 오름차순으로 근을 출력해주므로 주어진 범위를 오름차순으로 순회하며 방정식의 근을 찾아줍니다