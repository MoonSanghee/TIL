T = int(input())
# 테스트케이스의 수를 받아줍니다
for t in range(T):
    n = int(input())
    result = 0
    # 주어지는 원의 크기를 받고 결과를 담을 변수를 설정해줍니다
    for i in range(-n, n + 1):
        for j in range(-n, n + 1):
            if i * i + j * j <= n * n:
                result += 1
    # 주어지는 원를 포함하는 가장 작은 정사각형의 모든 좌표를 순회하며 원 안의 점들을 찾아줍니다
    print(f'#{t + 1} {result}')
    # 결과를 주어진 양식에 맞춰 출력해줍니다