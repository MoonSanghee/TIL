num = input()
# 수를 문자열 형태로 받아줍니다.
if num[0] == '0':
    # 문자열의 첫 자리가 '0'인지 확인하여 10진수인지 확인해줍니다.
    if num[1] == 'x':
    # 두 번째 자리가 x라면 16진수를 10진수 정수로 바꾸어주고
        number = int(num, 16)
    else:
    # 아니라면 8진수를 10진수로 바꾸어줍니다.
        number = int(num, 8)
else:
    number = int(num)

print(number)
# 정수로 전환한 수를 출력해줍니다.