t = int(input())
# 테스트케이스의 수를 받아줍니다
primes = []
superPrimes = []
# 소수와 슈퍼 소수를 담을 변수를 설정해줍니다
for i in range(2, 318138):
    for j in range(2, (int(i ** 0.5)) + 1):
        if i % j == 0:
            break
    else:
        primes.append(i)
# 주어진 예시를 통해 3000번째 슈퍼 소수가 318137임을 확인할 수 있으므로 
# 318137까지 에라스토테네스의 체를 이용하여 소수를 찾아줍니다
for i in range(3000):
    superPrimes.append(primes[primes[i] - 1])
# 3000번째까지의 슈퍼소수를 찾아 리스트에 담아줍니다
for _ in range(t):
    print(superPrimes[int(input()) - 1])
    # 찾는 순서의 슈퍼소수를 출력해줍니다