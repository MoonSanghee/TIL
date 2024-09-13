n, m = map(int, input().split())
# 학급수와 제한 인원을 받아줍니다.
d = dict()
students = []

while True:
    grade, name = input().split()
    if grade == name and grade == '0':
        break
    if d.get(grade, 0) < m:
        d[grade] = d.get(grade, 0) + 1
        students.append((grade, name))
    # 학급에서 학생을 추가할수있으면 리스트에 담아줍니다.
students.sort(key = lambda x: (int(x[0]), len(x[1]), x[1]))
# 학생을 학년, 이름의 길이, 사전수으로 정렬해줍니다.
white = []
blue = []

for i in range(len(students)):
    if int(students[i][0]) % 2 == 0:
        white.append(students[i])
    else:
        blue.append(students[i])
# 학급을 확인해 알맞은 팀에 배치해줍니다.
blue += white
# 청팀 다음에 백팀이 오므로 청팀 리스트에 백팀 학생 정보를 더해줍니다.
for i in blue:
    print(*i)
    # 학생의 정보를 차례대로 출력해줍니다.