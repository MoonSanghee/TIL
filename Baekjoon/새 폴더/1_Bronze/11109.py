t = int(input())
# 테스트케이스의 수를 받아줍니다
for tc in range(t):
    d, n, s, p = map(int, input().split())
    # 주어지는 정수들을 받아줍니다
    if d + p * n == n * s:
        print("does not matter")
    elif d + p * n > n * s:
        print("do not parallelize")
    else:
        print("parallelize")
    # 작업에 걸리는 시간을 비교하여 주어진 조건대로 출력해줍니다