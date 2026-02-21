t = int(input())
# 테스트 케이스가 몇 개 주어지는지 받아줍니다
for _ in range(t):
    n, m = map(int, input().split())
    # 상영관의 크기를 받아줍니다
    if m < 4 or n < 12:
        print(-1)
    else:
        print(11 * m + 4)
    # L4번 좌석이 존재하는지 확인하여 결과를 출력해줍니다