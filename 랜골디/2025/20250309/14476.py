from math import gcd

n = int(input())
numbers = sorted(list(map(int, input().split())))
# 주어지는 수들을 받아줍니다
left = [0] * n
left[0] = numbers[0]
for i in range(1, n):
    left[i] = gcd(left[i - 1], numbers[i])

right = [0] * n
right[-1] = numbers[-1]
for i in range(n - 2, -1, -1):
    right[i] = gcd(right[i + 1], numbers[i])
# 작은수부터 차례대로와 큰 수부터 차례대로 각 수들 까지의 최대공약수를 구하여줍니다
best = 0
k = -1
# 결과값을 담을 변수를 설정해줍니다
for i in range(n):
    if i == 0:
        num = right[1]
    elif i == n - 1:
        num = left[n - 2]
    else:
        num = gcd(right[i + 1], left[i - 1])
    # 각 인덱스의 값을 뺀 최대공약수를 구해줍니다
    if numbers[i] % num != 0 and num > best:
        best = num
        k = numbers[i]
    # 현재 인덱스 값을 뺀 최대 공약수가 현재 인덱스 값의 약수가 아니고 이전 기록된 값보다 크다면 값을 갱신해줍니다

if best == 0:
    print(-1)
else:
    print(best, k)
# 결과값을 출력해줍니다