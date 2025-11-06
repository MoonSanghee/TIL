while True:
    a, b = map(int, input().split())
    if a == b == 0:
        break
    print(f'{a // b} {a % b} / {b}')
# 주어진 입력에따라 결과를 출력해줍니다