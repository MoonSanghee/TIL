import sys
input = sys.stdin.readline

number = input().strip()
# 수를 문자열 형태로 받아줍니다.
n = 0
# 확인한 범위를 저장할 변수를 설정해줍니다.
while len(number):
    n += 1
    num = str(n)
    # n에 1을 더하고 문자열 형태로 바꾸어 변수에 담아줍니다.
    while len(num) and len(number):
        if num[0] == number[0]:
            number = number[1:]
        num = num[1:]
        # num과 number가 존재할때 한 자리씩 비교하며 수를 사용하였다면 한 자리씩 밀어줍니다.

print(n)
# number의 모든 수가 사용되었다면 n을 출력해줍니다.