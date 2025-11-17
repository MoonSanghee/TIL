n, m = map(int, input().split())
# 주어진 날과 목표 효과를 받아줍니다
effect = list(map(int, input().split()))
# 일자별 다이어트 효과를 받아줍니다
weight = sum(effect)
# 효과의 합을 구해줍니다
if weight < m:
    print(-1)
    # 목표에 도달할수없다면 -1을 출력해줍니다
else:
    for i in range(n):
        weight -= effect[i]
        if weight < m:
            print(i + 1)
            break
    # 하루씩 다이어트를 늦게 시작하였을때 목표에 도달할 수 있는지 확인하여 결과를 출력해줍니다