result = int(input())
# 결과를 담을 변수를 설정해줍니다
while True:
    command = input()
    if command == '=':
        print(result)
        break
    # 연산이 끝이나면 결과를 출력하고 작동을 멈추어줍니다
    elif command in '+-*/':
        past = command
    # 연산 기호가 나오면 임의의 변수에 담아줍니다
    else:
        command = int(command)
        if past == '+':
            result += command
        elif past == '-':
            result -= command
        elif past == '*':
            result *= command
        else:
            result //= command
        # 연산 기호가 아니라면 담겨있는 연산 기호를 확인해 연산을 진행해줍니다