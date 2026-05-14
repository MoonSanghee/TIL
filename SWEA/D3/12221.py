TC = int(input())
# 테스트케이스의 수를 받아줍니다
for t in range(TC):
    A, B = map(int, input().split())
    # 주어지는 두 수를 받아줍니다
    if A > 9 or B > 9:
        result = -1
    else:
        result = A * B
    # 한자리수가 아닌 수가 있는지 확인하여 결과를 구해줍니다
    print(f'#{t + 1} {result}')
    # 결과를 출력해줍니다