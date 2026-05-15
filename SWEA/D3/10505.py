T = int(input())
# 주어지는 테스트케이스의 개수를 받아줍니다
for t in range(T):
    N = int(input())
    numbers = list(map(int, input().split()))
    # 사람의 수와 사람들의 소득을 받아줍니다
    average = sum(numbers) / N
    result = 0
    # 평균값을 구하고 결과를 담을 변수를 설정해줍니다
    for i in numbers:
        if i <= average:
            result += 1
    # 소득을 순회하며 평균 이하의 소득을 가진 사람을 확인해줍니다
    print(f'#{t + 1} {result}')
    # 결과를 주어진 양식대로 출력해줍니다