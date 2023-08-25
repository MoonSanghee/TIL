while True:
    # 입력이있다면 계속 확인하여줍니다.
    try:
        coupon, need = map(int, input().split())
        chicken = 0
        # 쿠폰과 도장이 필요한 수를 받아줍니다.
        # 치킨을 주문한 수를 저장할 변수를 정해줍니다.
        stamp = coupon
        chicken += coupon
        # 치킨을 쿠폰만큼 시키고 도장을 받으므로 stamp와 chicken의 값을 
        # coupon으로 정해줍니다.
        while stamp // need:
            # 받은 도장으로 치킨을 주문할 수 있다면
            chicken += stamp // need
            # 가능한만큼 치킨을 받고
            stamp = stamp % need + stamp // need
            # 도장 값을 계산해줍니다.
        print(chicken)
        # 치킨의 값을 출력해줍니다.
    except:
        break