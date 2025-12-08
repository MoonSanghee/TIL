a, b, c = map(int, input().split())
# 주어지는 수들을 받아줍니다
if c == 0:
    print(int((a + b) ** (1 / 2)))
else:
    a, b = min(a, b), max(a, b)
    print(c ** 2 - b)
# 주어진 방식을 통해 빈칸의 수를 찾아 출력해줍니다