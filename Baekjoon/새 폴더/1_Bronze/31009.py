n = int(input())
costs = []
cnt = 0
for _ in range(n):
    city, cost = input().split()
    costs.append(int(cost))
    if city == 'jinju':result = int(cost)
for cost in costs:
    if cost > result:cnt += 1
# 주어지는 도시별 요금을 받아 진주행 요금을 확인하고 그보다 비싼 지역이 몇곳인지 확인해줍니다
print(result)
print(cnt)
# 결과를 차례대로 출력해줍니다