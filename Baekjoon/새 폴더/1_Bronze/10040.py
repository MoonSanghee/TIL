n, m = map(int, input().split())
costs = [int(input()) for _ in range(n)]
result = [0] * n
most = 0
# 경기와 심사위원의 수를 받고 경기의 비용을 받고 경기별 특표와 최다득표를 담을 변수를 설정해줍니다

for _ in range(m):
    limit = int(input())
    for i in range(n):
        if costs[i] <= limit:
            result[i] += 1
            if result[i] > most:
                most = result[i]
                most_number = i
            break
# 심사위원의 기준을 확인하며 최다 득표가 갱신되면 최다 득표 경기를 갱신하여줍니다
print(most_number + 1)
# 최다 득표 경기를 출력해줍니다