n = int(input())
students = [list(map(int, input().split())) for _ in range(n)]
# 학생의 수와 학생번호, 과목별 점수를 리스트 형태로 받아 담아줌니다.
result = []
# 과목별로 상품을 받을 수상자를 담을 리스트를 만들어줍니다.
for i in range(1, 5):
    score, number = 0, n + 1
    # 과목별로 순회하며 상품을 받을 최고점과 최고점자를 담을 변수를 설정해줍니다.
    # 점수는 0이상 100이하이고 최고점을 찾기때문에 0으로 설정해주고 번호는 n번 이하 1번 이상이고 
    # 동점의 경우 가장 번호가 작은 사람을 찾으므로 n + 1로 설정해줍니다.
    for j in range(n):
        if students[j][0] not in result:
            if students[j][i] > score:
                score = students[j][i]
                number = students[j][0]
            elif students[j][i] == score:
                number = min(number, students[j][0])
        # 상품을 받지 않았는지 확인하며 최고점이 갱신된다면 점수와 번호를 동점이라면 둘중 낮은 번호로 갱신해줍니다.
    result.append(number)
    # 모든 학생을 확인했다면 result에 과목별로 수상자를 받아줍니다.

print(*result)
# 결과를 출력해줍니다.