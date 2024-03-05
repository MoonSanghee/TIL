import math
c = int(input())
# 입력받는 경우의 수를 받아줍니다.
for _ in range(c):
    s, n, t, l = input().split()
    # 각 값을 입력받아줍니다.
    n = int(n)
    t = int(t)
    # n과 t를 정수로 전환시켜줍니다.
    limit = 10 ** 8 * int(l)
    # 1초에 10의 8승번 연산 가능하다고 주어졌으니 l의 정수형 값을 곱하여 제한범위를 구해줍니다.
    passed = False
    if s == "O(N)":
        if n * t <= limit:
            passed = True
    elif s == "O(N^2)":
        if ((n ** 2) * t) <= limit:
            passed = True
    elif s == "O(N^3)":
        if ((n ** 3) * t) <= limit:
            passed = True
    elif s == "O(2^N)":
        if ((2 ** n) * t) <= limit:
            passed = True
    else:
        if (math.factorial(n) * t) <= limit:
            passed = True
    # 주어진 조건을 계산해 연산이 시간내에 일어날 수 있는지 확인해줍니다.
    if passed:
        print("May Pass.")
    else:
        print("TLE!")
    # 연산을 시행한 결과를 출력해줍니다.