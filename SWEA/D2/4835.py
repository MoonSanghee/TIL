T = int(input())

for t in range(T):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    now = sum(a[:m])
    big, small = now, now

    for i in range(m, n):
        now -= a[i - m]
        now += a[i]

        big = max(big, now)
        small = min(small, now)
    
    print(f'#{t + 1} {big - small}')