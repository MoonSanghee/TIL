n = int(input())
result = 0
# 주어지는 선수의 수를 받고 결과를 담을 변수를 설정해줍니다
for _ in range(n):
    total = [0, 0, 0]
    points = list(map(int, input().split()))
    # 합계에 포함되는 3개의 점수를 담을 변수를 설정하고 전체 점수를 받아줍니다
    if points[0] > points[1]:
        total[0] = points[0]
    else:
        total[0] = points[1]
    for i in range(2, 7):
        if points[i] > total[1]:
            total[2] = total[1]
            total[1] = points[i]
        elif points[i] > total[2]:
            total[2] = points[i]
    # 각 종목별 점수를 확인해줍니다
    result = max(result, sum(total))
    # 최고점이 갱신되는지 확인해줍니다
print(result)
# 결과를 출력해줍니다