N, B, H, W = map(int, input().split())
result = 500001
# 주어지는 변수들을 받고 결과값을 담을 변수를 주어지는 비용의 범위보다 크게 설정해줍니다
for _ in range(H):
    cost = int(input())
    weeks = list(map(int, input().split()))
    # 비용과 주별로 남은 방의 정보를 받아줍니다
    if cost * N > B:continue
    # 방을 인원수 대로 예약할 때 예산을 초과한다면 다음 호텔을 확인해줍니다
    for i in weeks:
        if i >= N:
            result = min(result, cost * N)
            break
        # 방이 충분히 남은 주가 있다면 예약하는 비용과 현재 최소금액을 비교해 갱신해줍니다
if result > 500000:print("stay home")
else:print(result)
# 행사가 가능한지 확인하여 결과를 출력해줍니다