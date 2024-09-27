t = int(input())
# 테스트 케이스의 수를 받아줍니다.
for tc in range(t):
    line = input().split()
    number1, number2, answer = int(line[0]), int(line[2]), int(line[4])
    mark = line[1]
    # 연산을 진행할 수와 결과 연상기호를 받아줍니다.

    if mark == '+':
        result = number1 + number2
    elif mark == '-':
        result = number1 - number2
    elif mark == '*':
        result = number1 * number2
    elif mark == '/':
        result = number1 // number2
    # 연산 결과를 확인해줍니다.

    if result == answer:
        print('correct')
    else:
        print('wrong answer')
    # 주어진 결과와 실제 결과를 비교하고 결과에 따라 요청한 출력을 해줍니다.