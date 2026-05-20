T = int(input())
# 테스트케이스의 수를 받아줍니다
for t in range(T):
    n = int(input())
    # 주어지는 정수를 받아줍니다
    if n % 2:
        print(f'#{t + 1} {(n // 2) + 1}')
    else:
        print(f'#{t + 1} {-(n // 2)}')
    # 주어진 값에 따른 계산 결과를 주어진 양식대로 출력해줍니다