T = int(input())
# 테스트 케이스의 수를 받아줍니다
for t in range(T):
    P, Q, R, S, W = map(int, input().split())
    # 주어지는 변수들을 받아줍니다
    A = P * W
    if W <= R:
        B = Q
    else:
        B = Q + (W - R) * S
    # 두 회사의 요금을 구해줍니다
    print(f'#{t + 1} {min(A, B)}')
    # 요금이 저렴한쪽을 주어진 양식에 맞춰 출력해줍니다