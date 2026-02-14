while True:
    l, w, a = map(int, input().split())
    # 주어지는 입력을 받아줍니다
    if l == w == a and l == 0:
        break
    # 작동을 멈추는 입력인지 확인해줍니다
    elif l == 0:
        l = a // w
    elif w == 0:
        w = a // l
    else:
        a = l * w
    # 비어있는 값을 구해줍니다
    print(l, w, a)
    # 주어진 형식에 맞게 출력해줍니다