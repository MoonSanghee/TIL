n = int(input())
result = 6
# 주어지는 정수를 받고 결과에 6을 담아줍니다
while n != 10:
    result *= n
    n -= 1
# 10팩토리얼이 6주라는 값이 주어졌으므로 10에 도달할때까지 result에 n값을 곱하고 1을 빼줍니다
print(result)
# 결과값을 출력해줍니다