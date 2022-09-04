t = int(input())
for tc in range(1, t + 1):
    m, d =map(int, input().split())
    D = [4, 5, 6, 0, 1, 2, 3]
    days = 0
    while m != 1:
        if m in [2, 4, 6, 8, 9, 11]:
            days += 31
        elif m in [5, 7, 10, 12]:
            days += 30
        else:
            days += 29
        m -= 1
    if d != 1:
        days += d - 1
    print(f'#{tc} {D[days % 7]}')