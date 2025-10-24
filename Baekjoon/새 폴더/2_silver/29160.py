import heapq

n, k = map(int, input().split())
members = [[0] for _ in range(12)]
# 주어지는 변수를 받고 포지션별로 선수를 담을 리스트를 만들어줍니다
for _ in range(n):
    p, w = map(int, input().split())
    heapq.heappush(members[p], -w)
# 가치에 -를 붙여 힙푸시를 이용하여 가장 가치가 높은 선수가 맨 처음에 오도록 넣어줍니다
for _ in range(k):
    for i in range(1, 12):
        v = -heapq.heappop(members[i]) - 1
        if v < 0:
            v = 0
        heapq.heappush(members[i], -v)
    # 가치 하락을 적용하여줍니다
    # 단 가치는 0보다 낮아지지 않으므로 0보다 낮아지면 0으로 바꾸어줍니다
result = 0
for i in range(1, 12):
    result += - members[i][0]
print(result)
# 선발 선수의 가치 합을 구하여 출력해줍니다