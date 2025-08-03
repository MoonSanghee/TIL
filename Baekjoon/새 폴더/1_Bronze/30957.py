n = int(input())
students = input()
d = dict()
# 학생의 수와 선호하는 관심사를 받고 각 항목별 관심을 담을 변수를 설정해줍니다
for i in "BSA":
    d[i] = 0
for i in students:
    d[i] += 1
# 각 과목의 관심을 갱신해줍니다
most = 0
for i in "BSA":
    most = max(most, d[i])
# 가장 많은 관심의 값을 찾아줍니다

if d["B"] == d["S"] == d["A"]:
    print("SCU")
else:
    for i in "BSA":
        if d[i] == most:
            print(i, end='')
    # 주어진 형식에 맞춰 결과를 출력해줍니다