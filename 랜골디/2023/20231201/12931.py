n = int(input())
numbers = list(map(int, input().split()))
# 수의 개수와 각 자리 수를 받아줍니다.
cnt = 0
# 연산을 한 횟수를 담을 변수를 만들어줍니다.
while sum(numbers):
    # numbers의 합이 0이 되어 아무런 실행을 하기 전의 상태까지 연산을 계속합니다.
    check = 0
    # 연산을 진행하였는지 확인할 변수를 만들어줍니다.
    for i in range(n):
        if numbers[i] % 2:
            numbers[i] -= 1
            cnt += 1
            check = 1
    # numbers에 홀수가 있는지 확인하고 1을 뺀 후 연산을 했음을 표시해줍니다.
    if not check:
        for i in range(n):
            numbers[i] //= 2
        cnt += 1
    # 연산을 실행한 적 없다면 모두 짝수이므로 모든 수를 2로 나누어줍니다.

print(cnt)
# 연산을 실행한 수를 출력해줍니다.