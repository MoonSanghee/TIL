n, k = map(int, input().split())
# 얼음 양동이의 개수와 백곰이 닿는 범위를 받아줍니다.
ice = [0 for _ in range(1000001)]
# 얼음이 놓일수있는 좌표의 범위를 받아줍니다.
for _ in range(n):
    g, x = map(int, input().split())
    ice[x] = g
# 얼음이 위치한 범위를 표시해줍니다.
coming = 2 * k + 1
check = sum(ice[:coming])
# 시작점을 포함하여 최대의 얼음을 가지는 경우를 확인해줍니다.
result = check
# 최대값을 담을 변수를 설정해줍니다.
for i in range(coming, 1000001):
    check += ice[i]
    check -= ice[i - coming]
    result = max(result, check)
    # 새로 오는 좌표부터 닿지 않아지는 좌표의 값을 빼고 새로 닿는 좌표의 값을 더하며 최대값을 갱신해줍니다.

print(result)
# 결과를 출력해줍니다.