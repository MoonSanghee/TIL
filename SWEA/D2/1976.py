T = int(input())

for t in range(T):
    h1, m1, h2, m2 = map(int, input().split())
    h = h1 + h2
    m = m1 + m2

    if m >= 60:
        h += 1
        m %= 60
    
    if h >= 12:
        h %= 12
        if h == 0:
            h = 12
    
    print(f'#{t + 1} {h} {m}')