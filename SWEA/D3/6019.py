t = int(input())
for test in range(1, t + 1):
    d, a, b, f = map(int, input().split())
    print(f'#{test} {((d  * f) / (a + b))}')