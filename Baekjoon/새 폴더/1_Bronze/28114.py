team = []
for _ in range(3):
    p, y, s = input().split()
    p = int(p)
    y = str(int(y) % 100)
    team.append([p, y, s])
# 팀을 이루는 세 명의 정보를 받고 푼 문제수는 정수형 입학연도는 100으로 나눈 나머지의 문자열 형태로 변환하여 
# 리스트에 담아줍니다
year = sorted(team, key = lambda x : x[1])
problem = sorted(team, reverse = True)
# 입학 연도를 기준으로 오름차순 푼 문제수를 기준으로 내림차순으로 정렬한 두 리스트를 만들어줍니다
first = ''
second = ''
for i in range(3):
    first += year[i][1]
    second += problem[i][2][0]
# 정렬한 두 리스트에서 사용할 정보를 찾아 이름을 만들어줍니다
print(first)
print(second)
# 두 가지 방법으로 만들 팀명을 차례대로 출력해줍니다