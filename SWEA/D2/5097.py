T = int(input())
# 테스트케이스의 개수를 받아줍니다
for t in range(T):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    # 주어지는 변수들을 받아줍니다
    M %= N
    print(f'#{t + 1} {numbers[M]}')
    # 맨 앞의 수를 맨 뒤로 보내는 작업을 완료한 결과를 주어진 양식에 맞게 출력해줍니다