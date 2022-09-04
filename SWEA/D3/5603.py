t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    numbers = []
    for i in range(n):
        numbers.append(int(input()))
    cnt = 0
    avg = sum(numbers) // n
    for i in numbers:
        if i < avg:
            cnt += avg - i
    print(f'#{tc} {cnt}')