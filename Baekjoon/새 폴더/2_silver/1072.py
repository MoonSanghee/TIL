x, y = map(int, input().split())
z = (y * 100) // x
s, e = 1, 1000000000

if z >= 99:
    print(-1)
else:
    while s <= e:
        m = (s + e) // 2
        if (y + m) * 100 // (x + m) > z:
            e = m - 1
        else:
            s = m + 1
    print(e + 1)