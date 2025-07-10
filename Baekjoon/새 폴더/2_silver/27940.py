import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())
# 주어지는 층의 수와 비가 오는 횟수, 각 층이 버틸수 있는 빗물의 양을 받아줍니다
rain = 0
result = -1
# 전체 강수량과 무너졌다면 언제 무너졌는지를 담을 변수를 설정해줍니다
for i in range(m):
    t, r = map(int, input().split())
    # 비가 몇층까지 얼마나 내리는지 받아줍니다
    rain += r
    # 강수량을 더해줍니다
    if rain > k:
        if result == -1:
            result = i + 1
    # 강수량이 충분하다면 무너진 적 있는지를 확인하고 최초로 무너진 시간을 기록해줍니다
if result == -1:
    print(-1)
else:
    print(result, 1)
    # 무너지지 않았다면 -1, 무너졌다면 무너진 시간과 1층을 출력해줍니다.
    # 무너진 층 중에 아무 층이나 출력하면 되므로 무조건 무너지는 1층을 항상 출력하면 어디까지 무너지는지는 확인할 필요가 없습니다