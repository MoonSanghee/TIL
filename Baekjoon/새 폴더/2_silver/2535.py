n = int(input())
students = [list(map(int, input().split())) for _ in  range(n)]
# 학생의 수와 학생들의 정보를 받아줍니다.
students.sort(key = lambda  x : -x[2])
# 득점을 기준으로 내림차순 정렬을 해줍니다.
prize = [students[0], students[1]]
# 2명까지 국적이 같을수 있으므로 금상과 은상 학생의 정보를 수상목록에 넣어줍니다.
for i in range(2, n):
    if students[0][0] != students[1][0]:
        prize.append(students[2])
        break
    # 금상과 은상 수상자가 국적이 다르다면 동상은 국적에 상관없이 받을수있으므로 3번째 고득점자를 수상자에 넣고 반복을 멈추어줍니다.
    elif students[0][0] != students[i][0]:
        prize.append(students[i])
        break
    # 금상과 은상 수상자의 국적이 같다면 금상 수상자와 국적이 다른 학생이 나오면 수상자로 추가하고 반복을 멈추어줍니다.

for contry, number, point in  prize:
    print(contry, number)
    # 수상자 목록을 순회하며 국가 번호와 학생 번호를 차례대로 출력해줍니다.