n, m =map(int, input().split())
# 걸그룹의 수와 문제의 수를 받아줍니다.
d = dict()

for _ in range(n):
    team = input()
    cnt = int(input())
    members = []
    for _ in range(cnt):
        member = input()
        members.append(member)
        d[member] = team
    members.sort()
    d[team] = members
    # 팀이름과 팀원수를 받고 리스트에 팀 멤버들의 이름을 담아줍니다.
    # 팀 멤버들의 이름을 받으면서 이름을 키 값, 팀이름을 밸류값으로 딕셔너리에 담아줍니다.
    # 팀 멤버를 리스트에 다 담으면 리스트를 정렬하고 팀 이름과 멤버 목록을 딕셔너리에 담아줍니다.

for _ in range(m):
    problem = input()
    if int(input()):
        print(d[problem])
    else:
        for name in d[problem]:
            print(name)
    # 문제 유형을 받고 딕셔너리에 담긴 값을 출력해줍니다.