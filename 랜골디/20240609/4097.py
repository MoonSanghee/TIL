import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break
    # 0이 입력되면 작동을 멈추어줍니다.

    income = [int(input()) for _ in range(n)]
    result = [-10000 * n for _ in range(n + 1)]
    # 매일 수익을 담고 인덱스값이 1만큼 더 긴 dp 리스트를 만들어줍니다.

    for i in range(n):
        result[i + 1] = max(result[i] + income[i], income[i])
    # 연속하는것과 비교하여 더 값이 큰지 확인하여 값을 갱신해줍니다
    print(max(result))
    # 가장 큰 값을 찾아 출력해줍니다.