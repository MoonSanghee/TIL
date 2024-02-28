n = int(input())
# 정수를 받아줍니다.
result = 0
# 결과를 담을 변수를 설정해줍니다.
for i in range(1, n + 1):
    result += (n // i) * i
    # n을 i로 나눈 몫이 i개 까지 있을수 있으므로 result에 더해줍니다.
print(result)
# result에 담긴 값을 출력해줍니다.