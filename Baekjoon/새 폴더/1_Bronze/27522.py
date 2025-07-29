red, blue = 0, 0
# 양팀의 점수를 담을 변수를 설정해줍니다
score = [10, 8, 6, 5, 4, 3, 2, 1]
# 순위별 점수를 받아줍니다
records = []
for i in range(8):
    record, team = input().split()
    M, SS, sss = (map(int, record.split(":")))
    SS += M * 60
    sss += SS * 1000
    records.append((sss, team))
    # 기록과 팀 정보를 받고 튜플로 묶어 리스트에 담아줍니다

records.sort()
# 기록과 팀 정보가 담긴 리스트를 기록을 기준으로 오름차순 정렬을 해줍니다
for i in range(8):
    if records[i][1] == 'R':
        red += score[i]
    else:
        blue += score[i]
# 순위에 따라 각 팀에 점수를 더해줍니다
if red > blue:
    print('Red')
else:
    print('Blue')
    # 승리한 팀을 출력해줍니다