d = {'-': 0, '\\': 1, '(': 2, '@': 3, '?': 4, '>': 5, '&': 6, '%': 7, '/': -1}
# 각 문자에 매칭되는 수를 딕셔너리로 받아줍니다.
while True:
    number = input()
    if number == '#':
        break
    # '#'이 입력되면 작동을 멈추어줍니다.
    result = 0
    # 결과를 담을 변수를 설정해줍니다.
    for i in range(len(number)):
        result += d[number[i]] * 8 ** (len(number) - i - 1)
        # 8진수 값을 계산하여 결과에 더해줍니다.
    print(result)
    # 결과를 출력해줍니다.