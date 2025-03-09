n = int(input())
# 점의 개수를 받아줍니다.
d = dict()
# 색깔별로 점의 좌표를 저장해줄 딕셔너리를 만들어줍니다.
for _ in range(n):
    point, color = map(int, input().split())
    if color in d:
        d[color].append(point)
    else:
        d[color] = [point]
    # 색깔별로 점을 key값으로 딕셔너리에 리스트 형태로 넣어줍니다.

result = 0
# 화살표 길이의 합을 담을 변수를 설정해줍니다.
for key in d:
    d[key].sort()
    # 각 색깔별 좌표를 오름차순으로 정렬해줍니다.
    result += d[key][1] - d[key][0]
    result += d[key][-1] - d[key][-2]
    # 가장 첫 점과 마지막 점은 하나의 좌표와만 연결이 되므로 비교하지않고 바로 result에 값을 더해줍니다.

    for i in range(1, len(d[key]) - 1):
        result += min(d[key][i + 1] - d[key][i], d[key][i] - d[key][i - 1])
        # 각 색의 첫점과 마지막 점을 제외한 나머지 각 점들의 바로 전과 다음 점간의 길이중 작은 값을 result에 더해줍니다.

print(result)
# result값을 출력해줍니다.