n, m = map(int, input().split())
d = dict()
# 수업의 수와 기준을 받고 학생들이 받은 수업의 수를 담을 딕셔너리를 만들어줍니다
for _ in range(n):
    k = int(input())
    students = list(map(int, input().split()))
    for i in students:
        d[i] = d.get(i, 0) + 1
    # 수업을 들은 학생의 기록을 갱신해줍니다
result = 0
for i in d:
    if d[i] >= m:
        result += 1
# 각 학생을 확인하며 기준을 넘었다면 결과를 갱신해줍니다
print(result)
# 결과를 출력해줍니다