while True:
    A, B = map(int, input().split())
    # 사라의 인형수와 남겨둔 인형의 수를 받아줍니다
    if A == B == 0:
        break
    # 동작을 끝내는 입력인지 확인해줍니다
    dolls = A - B
    # 짝지을 인형의 수를 구해줍니다
    if dolls % 2 and dolls > 2:
        b = 1
        dolls -= 3
    else:
        b = 0
    # 3개인 무리가 있는지 확인해줍니다
    a = dolls // 2
    # 짝이 얼마나 존재하는지 구해줍니다
    print(a, b)
    # 결과를 출력해줍니다