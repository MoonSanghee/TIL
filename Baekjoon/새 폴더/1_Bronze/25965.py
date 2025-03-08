n = int(input())
# 총 게임수를 받아줍니다
for _ in range(n):
    m = int(input())
    missions = [list(map(int, input().split())) for _ in range(m)]
    kda = list(map(int, input().split()))
    # 총 미션의 수를 받고 미션들을 받고 게임 결과를 받아줍니다
    result = 0
    for i in range(m):
        price = missions[i][0] * kda[0] - missions[i][1] * kda[1] + missions[i][2] * kda[2]
        if price < 0:continue
        else:result += price
    # 각 미션별로 획득한 상금을 더해줍니다
    print(result)
    # 결과를 출력해줍니다