n, c = map(int, input().split())
m = int(input())
# 주어지는 마을의 수와 제한 용량, 보내는 박스 정보의 수를 받아줍니다
infomation = []
for _ in range(m):
    start, end, boxes = list(map(int, input().split()))
    infomation.append((start, end, boxes))
infomation.sort(key = lambda x : x[1])
# 보내는 박스 정보를 받고 받는 마을을 기준으로 정렬해줍니다
remain = [c] * (n + 1)
result = 0
# 각 마을별로 박스를 더 담을수 있는 공간을 확인할 변수를 만들고 운반하는 전체 박스의 수를 담을 변수를 설정해줍니다
for start, end, boxes in infomation:
    mimnum = min(remain[start:end])
    boxes = min(mimnum, boxes)
    # 운반 정보에서 운반하는 구간의 가장 적게 남은 여유 용량과 옮기려는 박스의 수중 가장 작은 값을 확인해줍니다
    for i in range(start, end):
        remain[i] -= boxes
    result += boxes
    # 기차가 이동하는 구간동안 옮길 박스의 수만큼 여유 공간을 빼줍니다

print(result)
# 전체 옮긴 박스의 수를 출력해줍니다