while True:
    # 입력이 있는지 확인해줍니다.
    try:
        A, B, C = map(int, input().split())
        print(max(B-A, C-B)-1)
        # 세 수를 받고 범위가 넓은 쪽에 1을 뺀만큼 이동이 가능합니다.
    except:
        break