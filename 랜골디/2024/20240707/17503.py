import heapq

n, m, k = map(int, input().split())
# 축제 일수와 원하는 만족도, 맥주의 종류가 몇개인지 받아줍니다.
beers = [list(map(int, input().split())) for _ in range(k)]
beers.sort(key = lambda x : [x[1], x[0]])
# 맥주의 도수와 만족도를 받고 도수, 만족도 순으로 정렬해줍니다.

result = 0
alcohol = []
# 마신 맥주별 만족도와 만족도의 합을 담을 변수를 설정합니다.
for u, v in beers:
    result += u
    heapq.heappush(alcohol, u)
    # 만족도의 합에 맥주의 만족도를 더하고 힙푸시를 이용하여 만족도를 담아줍니다.
    if len(alcohol) == n:
        # n개의 맥주를 골랐다면
        if result >= m:
            answer = v
            break
        # 만족도가 충분하다면 알코올 도수를 answer에 담고 확인을 멈춥니다.
        else:
            result -= heapq.heappop(alcohol)
        # 만족도가 부족하다면 heappop을 이용해 가장 만족도가 낮은것을 빼줍니다.
else:
    answer = -1
# 만족도가 충분해지는 조합이 없다면 answer에 -1을 담아줍니다.
print(answer)
# answer 값을 출력해줍니다.