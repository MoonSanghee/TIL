test = int(input())
for t in range(1, test + 1):
    a, b = map(int, input().split())
    print(f'#{t} {a+b}')
    # print('#{} {}'.format(t, a+b))