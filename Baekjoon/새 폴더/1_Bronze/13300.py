n, k = map(int, input().split())
# 학생의 수와 한 방에 들어갈 수 있는 제한 인원을 받아줍니다.
students = dict()
# 각 학년, 성별에 따라 학생들이 얼마씩있는지 저장해줄 딕셔너리를 만들어줍니다.
for _ in range(n):
    # 학생의 수만큼 정보를 받아줍니다.
    gender, grade = map(int, input().split())
    # 성별과 학년을 입력받아줍니다.
    student = (gender, grade)
    # 학생의 성별과 학년을 튜플로 묶어줍니다.
    students.setdefault(student, 0)
    # 딕셔너리에 학생의 정보가 없다면 기본값인 0으로 만들어줍니다.
    students[student] += 1
    # 해당 정보에 맞는 학생을 1명 더해줍니다.
rooms = 0
# 방의 수를 저장할 변수를 지정해줍니다.
for i in students:
    # 학생 정보를 순회하며
    rooms += students[i] // k
    # 해당 성별, 학년에 해당하는 학생을 k로 나눈 몫만큼 방을 더해주고
    if students[i] % k:
        rooms += 1
        # 몫이 아닌 나머지가 존재한다면 방이 1개 더 필요하니 1을 더해줍니다.

print(rooms)
# 필요한 방의 수를 출력해줍니다.