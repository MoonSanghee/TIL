T = int(input())
# 테스트케이스의 개수를 받아줍니다
for t in range(T):
    a, b, c = map(int, input().split())
    # 주어지는 상자의 사탕 개수들을 받아줍니다
    if b == 1 or c < 3:
        result = - 1
    elif c > b > a:
        result = 0
    # 만족시킬수 없는 경우와 사탕을 먹을수 없는 경우를 걸러줍니다
    else:
        result = 0
        if b >= c:
            result += b - c + 1
            b = c - 1
        if a >= b:
            result += a - b + 1
            a = b - 1
    # 사탕을 필요한만큼 먹어줍니다
    print(f'#{t + 1} {result}')
    # 결과를 주어진 양식에 맞게 출력해줍니다