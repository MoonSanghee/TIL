n = int(input())
result = 0
# 채점결과의 개수와 종합 점수를 담을 변수를 설정해줍니다
for _ in range(n):
    number = input()
    new = ''
    # 채점한 점수를 받아 줍니다
    if len(number) == 3:
        new = number
    # 수가 세자리라면 100이므로 그대로 유지해줍니다
    else:
        for i in number:
            if i in '069':
                new += '9'
            else:
                new += i
    # 수가 세자리가 아니라면 규칙에 따라 바꾸어줍니다
    result += int(new)
    # 수정한 점수로 점수를 바꾸어줍니다

if result / n - result // n >= 0.5: print(result // n + 1)
else:print(result // n)
# 평균값에 가까운 정수를 출력해줍니다