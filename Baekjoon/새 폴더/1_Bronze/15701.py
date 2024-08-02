n = int(input())
result = 0
# 주어지는 수와 숫자쌍의 개수를 담을 변수를 설정해줍니다. 
for i in range(1, int(n ** 0.5) + 1):
    # n 의 제곱근까지의 정수를 순회하며
    if n % i == 0:
        if i ** 2 == n:
            result += 1
        else:
            result += 2
    # n의 제곱근이라면 1쌍이 추가되고 제곱근이 아닌데 나누어떨어진다면 2쌍을 추가해줍니다

print(result)
# 결과를 출력해줍니다.