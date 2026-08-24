T = int(input())
# 테스트케이스의 개수를 받아줍니다
for tc in range(T):
    A, B, N = map(int, input().split())
    result = 1
    # 주어지는 변수들을 받고 연산 횟수를 담을 변수를 설정해줍니다
    while A + B <= N:
        if A > B:
            B += A
        else:
            A += B
        result += 1
    # 주어진 x, y 값중 큰값을 작은값에 더하는 것을 반복해 더한 결과가 목표에 도달할때까지 시행해줍니다
    print(result)
    # 결과를 출력해줍니다