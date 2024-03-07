t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print("yes")
    # a = a1 * a2, a` = a1 + a2일때 a2가 1라면 a` = a + 1이 될 수 있고 a보다 큰 모든 a`는 성립한다.
    # 그리고 a = a1 * -1 * -1 * 1라는 식으로 표현하면 a` = a - 1이되어 모든 작은 수도 성립한다.
    # 따라서 모든 두 정수에 대하여 답은 yes를 출력해주어야 한다.