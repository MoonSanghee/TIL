primes = []

for i in range(2, 1000):
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            break
    else:
        primes.append(i)
# 주어지는 정수 이하 범위에서 모든 소수를 찾아줍니다
T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    result = 0
    # 목표수를 받고 결과를 담을 변수를 설정해줍니다
    for i in range(len(primes)):
        if primes[i] < n:
            for j in range(i, len(primes)):
                if primes[i] + primes[j] < n:
                    for k in range(j, len(primes)):
                        if primes[i] + primes[j] + primes[k] == n:
                            result += 1
                        elif primes[i] + primes[j] + primes[k] > n:
                            break 
    # 소수를 조합하여 목표 수를 만들수 있는 조합의 개수를 찾아줍니다
    print(f'#{tc} {result}')
    # 결과를 출력해줍니다