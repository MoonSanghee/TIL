while True:
    try:
        n = int(input())
        if n % 6 == 0:
            print("Y")
        else:
            print("N")
    except:
        break
    # 입력을 받아 시침과 초침의 각도가 성립하는지 출력해줍니다