T = int(input())
# 테스트케이스의 수를 받아줍니다
for t in range(T):
    n = int(input())
    numbers = list(map(int, input().split()))
    # 주어지는 수의 개수와 수들을 받아줍니다
    print(f'#{t + 1} {max(numbers) - min(numbers)}')
    # 최댓값과 최소값의 차이를 주어진 양식에 맞게 출력해줍니다