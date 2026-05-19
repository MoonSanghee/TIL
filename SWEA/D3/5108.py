T = int(input())
# 테스트케이스의 수를 받아줍니다
for t in range(T):
    N, M, L = map(int, input().split())
    numbers = list(map(int, input().split()))
    # 주어지는 변수들과 수열을 받아줍니다
    for _ in range(M):
        idx, num = map(int, input().split())
        numbers.insert(idx, num)
    # 주어진 위치에 수를 넣어줍니다
    print(f'#{t + 1} {numbers[L]}')
    # 주어진 양식에 맞게 결과를 출력해줍니다