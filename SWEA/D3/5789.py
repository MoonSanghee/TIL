t = int(input())
for test in range(1, t + 1):
    n, q = map(int, input().split())
    num = [0 for _ in range(n)]
    for i in range(1, q + 1):
        l, r = map(int, input().split())
        for j in range(l - 1, r):
            num[j] = i
    print(f'#{test} ', end = '')
    print(*num)