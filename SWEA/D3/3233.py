test = int(input())
for t in range(1, test + 1):
    a, b = map(int, input().split())
    n = (a // b) ** 2
    print(f'#{t} {n}')