for i in range(2, 1000001):
    num = i
    number = int(i**(0.5))
    for j in range(2, number + 1):
        if num % j == 0:
            break
    else:
        print(i, end = ' ')

# 찾아본 코드
N = 10 ** 6 + 1
eratos = [1] * N
eratos[0], eratos[1] = 0, 0

for i in range(2, N // 2 + 1):
    if eratos[i] == 1:
        for j in range(i * 2, N, i):
            eratos[j] = 0

for i in range(N):
    if eratos[i] == 1:
        print(i, end=' ')
# N의 절반 만큼 순회하며 전체에 각 수들의 배수들을 표시해주고 표시 안 된 수들은 소수이므로 출력해준다.
