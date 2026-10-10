n = int(input())
factors = []

for i in range(n):
    i += 1
    if n % i == 0:
        factors.append(i)

for i in factors:
    print(f'{i}(은)는 {n}의 약수입니다.')