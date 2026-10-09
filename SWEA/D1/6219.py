n = int(input())
factors = []

for i in range(n):
    i += 1
    if n % i == 0:
        factors.append(i)

for i in factors:
    print(f'{i}(은)는 5의 약수입니다.')

if len(factors) == 2:
    print(f'{n}(은)는 {factors[0]}과 {factors[1]}로만 나눌 수 있는 소수입니다.')