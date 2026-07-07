T = int(input())

for t in range(T) :
    p = input().rstrip()
    q = input().rstrip()

    if p + "a" != q :
        print(f'#{t + 1} Y')
    else :
        print(f'#{t + 1} N')