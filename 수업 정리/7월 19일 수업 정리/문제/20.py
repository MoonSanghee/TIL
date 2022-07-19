# Q. 정수 number가 주어질 때, 각 자릿수의 합을 구해서 출력하세요. 
# Input
# 123

# A.
number = int(input())
number_sum = 0
while number // 10 != 0:
    number_sum += number % 10
    number //= 10
number_sum += number
print(number_sum)
