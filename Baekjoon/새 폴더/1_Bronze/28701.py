n = int(input())
# 주어지는 정수를 받아줍니다
first = 0
second = 0
third = 0
# 각 세가지 시뮬레이션을 작동한 결과를 담을 변수들을 설정해줍니다
for i in range(1, n + 1):
    first += i
    third += i ** 3
second = first ** 2
# 주어진 조건에 따라 계산을 실행해줍니다
print(first)
print(second)
print(third)
# 결과를 출력해줍니다