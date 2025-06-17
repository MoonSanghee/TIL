N = int(input())
schedule = [list(map(int, input().split())) for _ in range(N)]
# 놀이기구의 개수와 작동 시간을 받아줍니다
new = []
for start, end in schedule:
    startMinute = (start // 100) * 60 + start % 100 - 10
    endMinute = (end // 100) * 60 + end % 100 + 10
    new.append((startMinute, endMinute))
# 놀이기구 작동 시간을 분으로 환산하고 시작 시간 10분전 운행 종료 10분후까지 근무하므로 근무시간을 계산해 새로운 리스트에 담아줍니다
new.sort()
workEnd = 600
result = max(0, new[0][0] - 600)
# 운행시간을 시간시간을 기준으로 정렬하고 마지막 놀이기구의 운행 종료 시간을 일과 시작시간으로 맞추고 첫 놀이기구 운행전까지 휴식시간을 결과에 담아줍니다
for start, end in new:
    result = max(result, start - workEnd)
    workEnd = max(end, workEnd)
# 이전에 담긴 운행 종료시간과 확인하려는 놀이기구의 근무시작시간을 비교하여 휴식시간을 갱신하고 근무 마치는 시간도 갱신해줍니다
result = max(result, 1320 - workEnd)
print(result)
# 영업종료 시간과 근무 종료시간을 비교하여 마지막으로 갱신한 값을 결과와 비교하여 마지막에 결과값을 출력해줍니다