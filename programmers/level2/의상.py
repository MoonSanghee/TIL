def solution(clothes):
    clothes_type = dict()
    # 의상의 종류 별로 몇 개씩 가지는지 담을 딕셔너리를 설정합니다.
    for c, t in clothes:
        # 의상과 타입을 받아줍니다.
        if t not in clothes_type:
            clothes_type[t] = 1
        # 처음 받는 타입이라면 타입을 1개 받았다고 추가해줍니다.
        else:
            clothes_type[t] += 1
        # 받은적 있는 타입이라면 1개씩 추가해줍니다.

    cnt = 1
    # 조합의 수를 담을 변수를 설정해줍니다.
    for num in clothes_type.values():
        # 의상별로 몇가지 종류를 받는지 확인하여줍니다.
        cnt *= (num + 1)
        # 안 입는 경우도 있으므로 조합의 수에 의상 종류 +1을 곱하여줍니다.

    return cnt - 1
    # 아무 의상도 안 입는 경우는 안 되므로 cnt 값에 1을 빼줍니다.