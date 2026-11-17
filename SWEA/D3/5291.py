T = int(input())
numbers = [True for _ in range(1000001)]
numbers[0] = False
numbers[1] = False

# 주어진 범위안의 정수중 1이외의 약수를 가지는 수들을 찾아줍니다
for i in range(2, 1001):
    if numbers[i] == True:
        for j in range(i * 2, 1000001, i):
            numbers[j] = False

primes = []
# 남은 소수들을 리스트에 담아줍니다
for i in range(1000001):
    if numbers[i] == True:
        primes.append(i)

for tc in range(1, T + 1):
    # 주어지는 수의 범위를 받아줍니다
    a, b = map(int, input().split())
    result = 0
    idx = 0
    # 주어진 범위에 포함되는 모든 소수의 합을 구해줍니다
    while idx < len(primes):
        if primes[idx] >= b:
            break
        elif primes[idx] > a:
            result += primes[idx]
        idx += 1
    # 결과를 출력해줍니다
    print(f'#{tc} {result}')