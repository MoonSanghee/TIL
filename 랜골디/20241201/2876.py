n = int(input())
desks = [list(map(int, input().split())) for _ in range(n)]
# 책상의 수를 받고 학생의 등급을 받아줍니다
grade = [0, 0, 0, 0, 0]
result = [0, 0]
# 각 책상별로 최대 채점가능한 학생수를 담을 변수를 만들고 결과를 담을 변수도 만들어줍니다
for i in range(n):
    for j in range(5):
        # 각 책상을 확인하며
        if j + 1 not in desks[i]:
            grade[j] = 0
            # 해당 등급이 책상에 존재하지 않으면 연속할수 없다고 값을 갱신해줍니다
        else:
            grade[j] += 1
            if grade[j] > result[0]:
                result[0] = grade[j]
                result[1] = j + 1
            elif grade[j] == result[0] and j < result[1]:
                result[1] = j + 1
            # 해당 등급이 존재한다면 등급의 연속함을 갱신하고 최장 길이와 비교한 후 결과값을 갱신해줍니다

print(*result)
# 결과를 출력해줍니다