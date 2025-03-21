n, m = map(int, input().split())
routes = list(map(int, input().split()))
buses = [list(map(int, input().split())) for _ in range(n)]
# 버스를 타는 순서와 버스의 환승요금을 받아줍니다
result = 0
for i in range(m - 1):
    s, e = routes[i] - 1, routes[i + 1] - 1
    result += buses[s][e]
# 버스를 환승하며 드는 비용을 더해줍니다
print(result)
# 결과를 출력해줍니다