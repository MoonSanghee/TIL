first = input()
n = int(input())
result = 0
# 재수강할 과목 코드와 신청 가능한 과목의 수를 받고 결과를 담을 변수를 설정해줍니다
for _ in range(n):
    new = input()
    if first[:5] == new[:5]:
        result += 1
    # 앞자리 5개가 일치하는 과목을 찾아줍니다
print(result)
# 결과를 출력해줍니다