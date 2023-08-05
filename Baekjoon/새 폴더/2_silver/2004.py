n, k = map(int, input().split())

def count2(n):
    result = 0
    while n:
        n //= 2
        result += n
    return result
# 2의 개수를 세어주는 함수
# n이하의 정수중에서 2의 배수는 n을 나눈 몫만큼 존재하기에 n을 2로 나눈 몫을 더해줌.
# n을 2로 i번 나눌때 몫만큼 n이하 정수중에 2의 i제곱의 배수가 존재함.

def count5(n):
    result = 0
    while n:
        n //= 5
        result += n
    return result
# 같은 방식으로 n이하의 5의 배수를 세어줄 수 있음.

count10 = min(count2(n) - count2(k) - count2(n - k), count5(n) - count5(k) - count5(n - k))
print(count10)
# 0이 몇개로 끝나는것은 계산값에 10으로 몇 번 나누어 떨어지느냐이므로
# 2로 나누어 떨어지는 횟수와 5로 나누어 떨어지는 횟수중 적은쪽을 출력해줍니다.