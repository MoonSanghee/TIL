n = int(input())
d = dict()
# 근무표를 확인할 주의 수와 근무자별 근무시간을 담을 변수를 설정해줍니다
for _ in range(n):
    for i in range(4):
        schedule = list(input().split())
        for j in schedule:
            if j == '-':
                continue
            else:
                if i == 0:
                    d[j] = d.get(j, 0) + 4
                elif i == 1:
                    d[j] = d.get(j, 0) + 6
                elif i == 2:
                    d[j] = d.get(j, 0) + 4
                else:
                    d[j] = d.get(j, 0) + 10
        # 근무 주동안 각 시간대별로 근무자가 있다면 시간을 더해줍니다
if len(d) == 0:
    print("Yes")
else:
    work_times = list(d.values())
    if max(work_times) - min(work_times) <= 12:
        print("Yes")
    else:
        print("No")
# 근무자가 있고 근무시간이 공정한지 확인하여 결과를 출력해줍니다