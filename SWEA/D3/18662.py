T = int(input())
# 테스트케이스의 개수를 받아줍니다
for t in range(T):
    a, b, c = map(int, input().split())
    result = abs(2 * b - a - c) / 2
    # 주어진 세 수를 받고 더하거나 빼주어야하는 수를 구해줍니다
    print(f'#{t + 1} {result}')
    # 결과를 주어진 양식에 맞게 출력해줍니다