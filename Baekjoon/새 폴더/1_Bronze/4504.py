n = int(input())
# 나누어 확인할 수를 받아줍니다.
while True:
    num = int(input())
    if num == 0:
        break
    # 0이 입력될때까지 반복하여줍니다.
    if num % n:
        print(f'{num} is NOT a multiple of {n}.')
    else:
        print(f'{num} is a multiple of {n}.')
    # 새로 입력받은 수가 나누어떨어지는지 확인하고 결과에 맞게 출력해줍니다.