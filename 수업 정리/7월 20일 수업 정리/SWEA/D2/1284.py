T = int(input())
for i in range(T):
    P, Q, R, S, W = map(int, input().split())
    a = P * W
    if W > R:
        b = Q + (S * (W - R))
    else :
        b = Q
    if a < b:
        print(f'#{i + 1}', end = ' ')
        print(a, end = ' ')
        print()
    else:
        print(f'#{i + 1}', end = ' ')
        print(b, end = ' ')
        print()