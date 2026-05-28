T = int(input())
# 테스트케이스의 수를 받아줍니다
for t in range(T):
    N, K = map(int, input().split())
    numbers = list(map(int, input().split()))
    # 전체 학생수와 과제를 제출한 학생의 수를 받고 과제를 제출한 학생들의 번호를 받아줍니다
    result = ''
    for i in range(N):
        if i + 1 not in numbers:
            result += ' ' + str(i + 1)
    # 과제를 제출하지 않은 학생들을 받아줍니다
    print(f'#{t + 1}{result}')
    # 결과를 주어진 양식에 맞게 출력해줍니다