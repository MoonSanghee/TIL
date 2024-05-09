a, b, c = map(int, input().split())
i, j, k = map(int, input().split())
# 필요한 음료의 비율과 주어지는 음료를 받아줍니다.
t = min(a / i, b / j, c / k)
print(a - i * t, b - j * t, c - k * t)
# 만들수있는 음료의 최대량을 구하고 각 재료별로 음료를 만들고 남은 양을 구해 출력해줍니다.