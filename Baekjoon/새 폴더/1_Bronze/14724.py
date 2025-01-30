clubs = ['PROBRAIN', 'GROW', 'ARGOS', 'ADMIN', 'ANT', 'MOTION', 'SPG', 'COMON', 'ALMIGHTY']
# 주어지는 동아리를 우선순위대로 리스트에 담아줍니다
n = int(input())
solved = 0
number = 0
# 동아리원이 몇명인지 받고 가장 많이 푼 수와 동아리 번호를 담을 변수를 설정해줍니다
for i in range(9):
    highest = max(list(map(int, input().split())))
    if highest > solved:
        solved = highest
        number = i
    # 각 동아리별 푼 문제를 모두 받고 최고점이 갱신되는지 확인하여 값이 갱신되며 동아리값도 갱신해줍니다
print(clubs[number])
# 결과를 출력해줍니다