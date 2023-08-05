n = int(input())
# 정수를 입력받아줍니다.
result = 0
# 몫과 나머지가 같은 수들을 모두 더한 값을 저장할 변수를 정해줍니다.
for num in range(n + 1, n ** 2, n + 1):
    result += num
    # n + 1부터 n의 제곱까지 n + 1 마다 result에 더해줍니다.
print(result)
# result값을 출력해줍니다.