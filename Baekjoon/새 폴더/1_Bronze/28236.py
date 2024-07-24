n, m, k = map(int, input().split())
# 학교의 크기와 경쟁하는 반의 수를 받아줍니다
result = 0
distance = 200000
# 우승 학급을 담을 변수와 최단 거리를 담을 변수를 설정해줍니다.
# 최단거리는 넓이와 높이가 최대 10만씩이므로 둘을 합한 20만으로 설정해줍니다.
for i in range(1, k + 1):
    f, d = map(int, input().split())
    cost = n - d + f - 1
    if cost < distance:
        distance = cost
        result = i
    # 각 학급을 차례대로 현재까지 최단거리와 비교해 급식실까지 더 가까운 학급이 존재하면 거리와 학급 값을 갱신해줍니다.

print(result)
# 결과를 출력해줍니다.