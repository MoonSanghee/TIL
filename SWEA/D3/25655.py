T = int(input())
# 주어지는 테스트케이스의 개수를 받아줍니다
for _ in range(T):
    X = int(input())
    # 정수를 받아줍니다
    result = ''
    # 결과를 담을 변수를 설정해줍니다
    if X == 1:
        result = 0
        # X가 1이라면 0으로 시작할 수 있으므로 결과가 0입니다
    else:
        if X %2:
            result += '4'
        result += '8' * (X // 2)
    print(result)
    # 결과를 출력해줍니다