T = int(input())

for tc in range(1, T + 1):
    n = int(input())

    result = n * 2

    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            result = min(result, i + n // i - 2)
    
    print(f'#{tc} {result}')