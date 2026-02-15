t = int(input())
# 주어지는 테스트케이스의 수를 받아줍니다
for _ in range(t):
    n = int(input())
    if n % 25 >= 17:
        print('OFFLINE')
    else:
        print('ONLINE')
    # 주어지는 수를 받아 결과를 출력해줍니다