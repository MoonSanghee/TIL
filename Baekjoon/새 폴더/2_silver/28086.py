code = input()
# 주어지는 수식을 받아줍니다
for i in range(1, len(code)):
    if code[i] not in '01234567':
        A = code[:i]
        B = code[i + 1:]
        sign = code[i]
        break
    # 연산자를 기준으로 두 수와 연산자를 구해줍니다
B = code[len(A)+1:]
A = int(A, 8)
B = int(B, 8)
flag = True
# 두 수를 8진수로 변환하고 계산이 가능한지 담을 변수를 설정해줍니다
if sign == '/':
    if B == 0:
        print('invalid')
        flag = False
    else:
        result = A // B
    # 나눗셈일경우 나누는값이 0일경우 연산이 불가하므로 정해진값을 출력하고 연산이 불가함을 표시해줍니다
elif sign == '-':
    result = A - B
elif sign == '*':
    result = A * B
else:
    result = A + B
# 10진수로 계산한 결과를 구해줍니다
if flag:
    if result < 0:
        print('-' + oct(abs(result))[2:])
    else:
        print(oct(result)[2:])
    # 연산 결과를 8진수로 변경하여 결과를 출력해줍니다