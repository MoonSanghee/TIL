import sys
input = sys.stdin.readline

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    # 0, 0을 입력받으면 확인을 멈추어줍니다.
    base = dict()
    for _ in range(n):
        base[int(input())] = True
    # 상근이의 리스트를 받아줍니다.
    cnt = 0
    for _ in range(m):
        if int(input()) in base:
            cnt += 1
    # 선영이의 리스트를 상근이의 리스트와 비교하며 둘 다 가지고 있는경우 표시해줍니다.
    print(cnt)
    # 둘 다 가지고 있는 갯수를 출력해줍니다.