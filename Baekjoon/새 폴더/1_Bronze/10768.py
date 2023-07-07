m = int(input())
d = int(input())
# 달과 일자를 순서대로 받아줍니다.
if m == 2 and d == 18:
    print('Special')
    # 2월 18일이면 Special을 출력합니다.
elif (m == 2 and d < 18) or m == 1:
    print('Before')
    # 2월 18일 이전이면 Before를
else:
    print('After')
    # 나머지의 경우 After를 출력해줍니다.