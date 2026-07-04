T = int(input())
# 테스트케이스의 개수를 받아줍니다
for t in range(T):
    A, B, C, D = map(int, input().split())
    # 주어지는 변수들을 받아줍니다
    s = max(A, C)
    e = min(B, D)
    result = e - s
    # 두 전구가 같이 켜져있는 시간을 확인해줍니다
    if result < 0:
        result = 0
    print(f'#{t + 1} {result}')
    # 결과를 주어진 양식에 맞게 출력해줍니다