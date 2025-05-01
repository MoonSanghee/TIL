t = int(input())
# 테스트 케이스의 수를 받아줍니다
for _ in range(t):
    n = input()
    # 주어지는 수를 받아줍니다
    middle = 5 * (10 ** (len(n) - 1)) - 1
    number = ''
    number2 = ''
    # 자릿수가 하나 큰 10의 제곱수의 반과 그 값에 1을 뺀 값의 곱이 그 자릿수의 가장 사랑스러운 값이고 
    # n이 그보다 작다면 n과 n을 반전한 값의 곱이 가장 사랑스러운 수입니다

    if int(n) >= middle:
        number = middle
        number2 = middle + 1
    else:
        number = int(n)
        for i in n:
            number2 += str(9 - int(i))
        number2 = int(number2)
    # 가장 사랑스러운 수 쌍을 찾아줍니다
    print(number * number2)
    # 두 수의 곱을 출력해줍니다