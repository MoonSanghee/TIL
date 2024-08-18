n = int(input())
# 득점이 일어난 횟수를 받아줍니다.
team_one_lead = 0
team_two_lead = 0
# 두 팀이 리드를한 시간을 담을 변수를 설정해줍니다.
score = 0
# 리드를 하고있는 팀을 확인하기 위해 득점이 발생했을때 어느팀이 얼마나 리드하는지 담을 변수를 설정해줍니다.
get_lead_time = 0
# 최근 점수가 바뀐 시간을 담을 변수를 설정해줍니다.
for i in range(n):
    team, time = input().split()
    m, s = map(int,time.split(":"))
    # 득점한 팀과 시간을 받고 분과 초로 나누어줍니다.
    
    if team == '1':
        if score == 0:
            team_one_lead += 48 * 60 - (60 * m + s)
        score += 1
        if score == 0:
            if team_two_lead > 0:
                team_two_lead -= 48 * 60 - (60 * m + s)
        # 1팀이 득점하였다면 리드가 어디였는지 확인하고 리드 시간을 갱신하고 득점을 표시해줍니다.
    else:
        if score == 0:
            team_two_lead += 48 * 60 - (60 * m + s)
        score -= 1
        if score == 0:
            if team_one_lead > 0:
                team_one_lead -= 48 * 60 - (60 * m + s)
        # 2팀이 득점하였다면 리드를 확인하고 리드 시간과 득점을 갱신해줍니다.

print("{:0>2}:{:0>2}".format(team_one_lead // 60, team_one_lead % 60))
print("{:0>2}:{:0>2}".format(team_two_lead // 60, team_two_lead % 60))
# 알맞은 포맷에 맞게 결과를 출력해줍니다.