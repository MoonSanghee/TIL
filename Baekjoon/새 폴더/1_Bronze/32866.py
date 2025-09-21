n = int(input())
x = int(input())
left = n * (100 - x) / 100
# 주어지는 변수를 통해 남은 금액을 구해줍니다
result = n / left - 1
print(round(result * 100, 6))
# 원금을 복구하기위해 얼마가 필요한지 구하여 요청받은 자릿수에 맞게 출력해줍니다