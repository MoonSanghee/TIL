T = int(input())
# 테스트케이스의 수를 받아줍니다
for t in range(T):
    A, B, C = map(int, input().split())
    # 빵의 가격과 가진 돈을 받아줍니다
    result = max(C // A, C // B)
    print(f'#{t + 1} {result}')
    # 최대로 살 수 있는 빵의 수를 주어진 양식대로 출력해줍니다