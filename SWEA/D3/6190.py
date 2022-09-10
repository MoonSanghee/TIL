t = int(input())
for test in range(1, t + 1):
    n = int(input())
    numbers = list(map(int, input().split()))
    numbers.sort(reverse=True)
    best = 0
    for i in range(n):
        for j in range(i + 1, n):
            num = numbers[i] * numbers[j]
            if num > best:
                if list(map(int, str(num))) == sorted(list(map(int, str(num)))):
                    if num > best:
                        best = num

    if best == 0:
        print(f'#{test} -1')
    else:
        print(f'#{test} {best}')