while True:
    n = int(input())
    # 주어지는 정수를 받아줍니다
    if n == 0:
        break
    # 마지막 입력인지 확인해줍니다
    for i in range(n):
        print('*' * (i + 1))
    # 마지막이 아니라면 요청받은 크기의 삼각형을 출력해줍니다