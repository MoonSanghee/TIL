test = int(input())
for t in range(1, test + 1):
    n = int(input())
    a = (n*(n+1))//2
    b = (n*(2*n))//2
    c = (n*(2*n+2))//2
    x = [t, a, b, c]
    print(f'#{t} {a} {b} {c}')
    # print('#', end = '')
    # print(*x)