T = int(input())
# 테스트케이스의 개수를 받아줍니다
for t in range(T):
    n = int(input())
    p = list(map(int ,input().split()))
    result = 0
    # 주어지는 수의 개수와 수열을 받고 결과를 담을 변수를 설정해줍니다
    for i in range(1, n - 1):
        if p[i - 1] < p[i] < p[i + 1] or p[i + 1] < p[i] < p[i - 1]:
            result += 1
    # 수열의 각 자리 수가 보통수인지 확인해줍니다
    print(f'#{t + 1} {result}')
    # 결과를 주어진 양식에 맞게 출력해줍니다