sum = 0
cnt = 0
# 학점 * 과목평점을 넣어줄 변수와 이수 학점을 넣어줄 변수를 설정해줍니다.
mark = {'A+' : 4.5, 'A0' : 4.0, 'B+' : 3.5, 'B0' : 3.0, 'C+' : 2.5, 
        'C0' : 2.0, 'D+' : 1.5, 'D0' : 1.0, 'F' : 0}
# 각 등급의 점수를 등급, 점수를 키, 밸류 쌍으로 딕셔너리에 저장해줍니다.

for _ in range(20):
    classname, credit, grade = input().split()
    # 20번에 거쳐서 받은 3개의 입력값을 과목명, 이수 학점, 등급으로 나누어 받아줍니다.
    if grade in mark:
        sum += mark[grade] * int(credit[0])
        cnt += int(credit[0])
        # 등급이 패스가 아니면 딕셔너리에서 찾아 밸류와 이수 학점을 곱한 값을
        # sum에 넣어주고 이수 학점을 cnt에 넣어줍니다. 

result = round(sum / cnt, 6)
# round함수를 이용하여 소수점 7번째 자리에서 반올림해줍니다. 
print(result)
# 결과갑을 출력해줍니다.