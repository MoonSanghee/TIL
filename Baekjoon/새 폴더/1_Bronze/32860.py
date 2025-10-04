n, m = map(int, input().split())
# 주어지는 변수를 받아줍니다
if m <= 26:
    print(f'SN {n}{chr(m % 27 + 64)}')
elif m % 26 == 0:
    print(f'SN {n}{chr(m // 26 + 95)}{chr(122)}')
else:
    print(f'SN {n}{chr(m // 26 + 96)}{chr(m % 26 + 96)}')
# 결과를 출력해줍니다