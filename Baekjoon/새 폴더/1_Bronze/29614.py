s = input()
# 주어지는 문자열을 받아줍니다
points = 0
cnt = 0
# 학점의 누적합과 전체 과목수를 받을 변수를 설정해줍니다
for i in range(len(s)):
    if s[i] == "+":
        continue
    elif s[i] == 'A':
        points += 4
    elif s[i] == 'B':
        points += 3
    elif s[i] == 'C':
        points += 2
    elif s[i] == 'D':
        points += 1
    cnt += 1
    if i != len(s) - 1:
        if s[i + 1] == '+':
            points += 0.5
# 주어지는 학점을 더하고 과목값을 갱신해줍니다
print(points / cnt)
# 평균 학점을 출력해줍니다