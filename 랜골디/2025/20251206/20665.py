n, t, p = map(int, input().split())
schedule = [[] for _ in range(721)]
result = 0
booking = []
# 주어지는 변수들을 받고 예약 정보와 각 시간별로 이용하는 정보, 결과를 담을 변수를 설정해줍니다
for _ in range(t):
    start, end = input().split()
    sh = start[:2]
    sm = start[2:]
    eh = end[:2]
    em = end[2:]
    info = (int(sh) * 60 + int(sm) - 540, int(eh) * 60 + int(em) - 540)
    booking.append(info)
# 각 시작 시간과 끝나는 시간을 묶어 리스트에 담아줍니다
booking.sort()
# 예약 기록을 시작시간을 기준으로 정렬해줍니다
for i in range(t):
    start, end = booking[i][0], booking[i][1]
    if not schedule[start]:
        for j in range(start, end):
            schedule[j].append(1)
        # 사용하고있는 자리가 없다면 1번 자리를 사용하도록 해줍니다
    else:
        schedule[start].sort()
        if schedule[start][0] - 1 >= n - schedule[start][-1]:
            seat = 1
            distance = schedule[start][0] - 1
        else:
            seat = n
            distance = n - schedule[start][-1]
        # 사용하고있는 자리가 있다면 일단 사용하고있는 자리중 1번과 마지막 번호중 멀리 떨어진 자리와 거리를 설정해줍니다
        for j in range(1, len(schedule[start])):
            if (schedule[start][j] + schedule[start][j - 1]) // 2 - schedule[start][j - 1] > distance:
                distance = (schedule[start][j] - schedule[start][j - 1]) // 2
                seat = (schedule[start][j] + schedule[start][j - 1]) // 2
            elif(schedule[start][j] + schedule[start][j - 1]) // 2 - schedule[start][j - 1] == distance:
                seat = min(seat, (schedule[start][j] + schedule[start][j - 1]) // 2)
            # 거리가 더 먼 경우가 존재한다면 더 먼 자리로 갱신하고 같은 거리가 있다면 숫자가 작은 좌석으로 변경해줍니다
        for k in range(start, min(end, 720)):
            schedule[k].append(seat)
            # 예약 시간동안 사용할 자리를 설정해줍니다

for i in range(720):
    if p not in schedule[i]:
        result += 1
print(result)
# 원하는 자리가 사용 가능한 시간을 확인학 결과를 출력해줍니다