tc = 0
while True:
    a, operator, b = input().split()
    if operator == 'E':
        break
    tc += 1
    # 주어지는 두 수와 비교 연산자를 받고 테스트 케이스를 갱신해줍니다
    a, b = int(a), int(b)
    flag = False
    # a, b를 정수로 바꾸고 유효한지 확인할 변수를 만들어줍니다
    if operator == '>' and a > b:
        flag = True
    elif operator == '>=' and a >= b:
        flag = True
    elif operator == '<' and a < b:
        flag = True
    elif operator == '<=' and a <= b:
        flag = True
    elif operator == '==' and a == b:
        flag = True
    elif operator == '!=' and a != b:
        flag = True
    
    if flag:
        print(f'Case {tc}: true')
    else:
        print(f'Case {tc}: false')
    # 결과를 출력해줍니다