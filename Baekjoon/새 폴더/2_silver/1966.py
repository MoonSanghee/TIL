from collections import deque
t = int(input())
# 테스트 케이스의 수를 받아줍니다
for tc in range(t):
    n, m = map(int, input().split())
    numbers = deque(list(map(int, input().split())))
    result = 0
    # 주어지는 변수들을 받고 몇 개의 수가 출력되었는지 담을 변수를 설정해줍니다
    while numbers:
        if numbers[0] < max(numbers):
            numbers.append(numbers.popleft())
        else:
            result += 1
            if m == 0:
                break
            numbers.popleft()
        if m > 0: m -= 1
        else: m = len(numbers) - 1
    # 중요도가 더 높은 수가 있는지 확인하고 숫 빼주고 목표했던 수의 위치가 움직인것을 수정해 목표한 수가 빠져나올때까지 시행합니다
    print(result)
    # 결과를 출력해줍니다