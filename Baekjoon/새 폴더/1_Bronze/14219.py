n, m = map(int, input().split())

if n % 3 == 0 or m % 3 == 0:
    print('YES')
else:
    print('NO')
    # 3의 배수가 있으면 YES 아니면 NO를 출력해줍니다