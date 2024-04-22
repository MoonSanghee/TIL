away = list(map(int, input().split()))
home = list(map(int, input().split()))
# 두 팀의 공격 결과를 받아줍니다.
lead = 0
upset = False
# 울림 기준으로 리드하는 점수를 담을 변수와 역전이 나왔는지 확인할 변수를 설정해줍니다.
for i in range(9):
    lead += away[i]
    # 울림의 공격을 먼저 반영해줍니다.
    if lead > 0 and home[i] > lead:
        upset = True
    # 역전이 나왔는지 확인해줍니다.
    lead -= home[i]
    # 울림의 수비 결과를 반영해줍니다.

if lead < 0 and upset:
    print('Yes')
else:
    print('No')
# 역전이 나왔고 결과적으로 경기를 졌다면 Yes 아니면 No를 출력해줍니다