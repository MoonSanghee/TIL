n = int(input())
number = bin(n)[2:][::-1]
now, result = 1, 0
# 주어지는 차례를 받고 2진수로 바꾸어 뒤집어줍니다
# 현재 제곱수의 값고 결과값을 담을 변수를 설정해줍니다
for i in number:
    result += now * int(i)
    now *= 3
# 현재 제곱수를 사용할지를 확인하여 결과에 더해줍니다
print(result)
# 결과를 출력해줍니다