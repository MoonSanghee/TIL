N, M = map(int, input().split())
numbers = list(map(int, input().split()))

result = 0

for i in range(N):
    for j in range(1 + i, N):
        for k in range(1 + j, N):
            sum = numbers[i] + numbers[j] + numbers[k]
            if result < sum <= M:
                result = sum

print(result)