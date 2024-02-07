import sys
input = sys.stdin.readline

t = int(input())
# 받을 수의 개수를 받아줍니다.
for _ in range(t):
    n = int(input())
    # 정수를 받아줍니다.
    cnt = 0
    i = 5
    while i <= n:
        cnt += n // i
        i *= 5
    # n이하의 5의 n승인 정수를 몇개 가지는지 확인해줍니다.
    print(cnt)
    # cnt에 담긴 0의 개수를 출력해줍니다.