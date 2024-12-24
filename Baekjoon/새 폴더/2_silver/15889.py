n = int(input())
friends = list(map(int, input().split()))
# 전우의 수와 위치를 받아줍니다
if n == 1:
    print("권병장님, 중대장님이 찾으십니다")
    # 주어지는 전우가 1명이라면 무조건 게임을 마무리할수 있습니다
else:
    power = list(map(int, input().split()))
    limit = power[0]
    # 각 전우가 던질수있는 제한범위를 받고 욱제가 던질수있는 위치의 정보를 받아줍니다
    for i in range(1, n):
        if friends[i] > limit:
            print("엄마 나 전역 늦어질 것 같아")
            break
        # 전우의 위치가 던질수 있는 위치보다 멀다면 게임을 조용히 마무리 할 수 없습니다
        elif i == n - 1:
            print("권병장님, 중대장님이 찾으십니다")
            break
        # 마지막 전우에게 수류탄이 전달 된다면 조용히 마무리 할 수 있습니다 
        else:
            limit = max(limit, friends[i] + power[i])
        # 제한 범위를 각 전우가 다시 던지는 것과 이전 제한범위를 비교하여 갱신해줍니다