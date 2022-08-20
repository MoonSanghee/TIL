test = int(input())
for t in range(1, test + 1):
    n, m = map(int, input().split())
    maxi = 2 * m
    two = maxi - n
    one = m - two
    print(f'#{t} {two} {one}')