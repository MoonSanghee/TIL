while True:
    try:
        m, p, l, e, r, s, n = map(int, input().split())
        # 주어지는 입력을 받아줍니다
        for _ in range(n):
            result = m
            m = p // s
            p = l // r
            l = result * e
        print(m)
        # 모기의 수를 출력해줍니다
    except:
        break