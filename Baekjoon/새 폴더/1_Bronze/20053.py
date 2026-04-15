T = int(input())
# 테스트 케이스의 수를 받아줍니다
for _ in range(T):
    n = int(input())
    numbers = sorted(list(map(int, input().split())))
    # 주어진 정수의 개수와 주어지는 정수들을 받고 오름차순으로 정렬해줍니다
    print(numbers[0], numbers[-1])
    # 최소값과 최대값을 출력해줍니다