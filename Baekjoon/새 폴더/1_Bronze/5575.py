for _ in range(3):
    h1, m1, s1, h2, m2, s2 = map(int, input().split())
    # 3명의 출근과 퇴근 시간을 차례대로 받아줍니다.
    t1 = h1*60*60 + m1*60 + s1
    t2 = h2*60*60 + m2*60 + s2
    t = t2 - t1
    # 출근과 퇴근시간을 초로 바꾸어 퇴근 시간에서 출근 시간을 빼줍니다.
    h = t//60//60 % 24
    m = t//60 % 60
    s = t%60
    print(h, m, s)
    # 나온 값을 시간, 분, 초로 다시 바꾸어 출력해줍니다.