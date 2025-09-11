import sys

n = input()
p = n[2:]
q = 10 ** (len(p) - 2)
# 주어지는 변수를 받고 변수가 소수점 아래 부분과 자릿수를 이용하여 정수, 10의 배수를 분자, 분모로 받아줍니다
print("YES")
print(int(p), q)
# 결과를 출력해줍니다