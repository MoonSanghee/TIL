import sys
input = sys.stdin.readline
n, m = map(int, input().split())
rooms = [0] * n
# 방의 수와 요청의 수를 받고 각 방이 언제까지 사용중인지 담을 변수를 만들어줍니다
for _ in range(m):
    number, start, end = map(int, input().split())
    if rooms[number - 1] <= start:
        rooms[number - 1] = end
        print("YES")
    else:
        print("NO")
    # 주어지는 예약의 방을 예약하려는 시간에 이용중인지를 확인하여 결과를 출력해줍니다