t = int(input())
check = dict()
for i in range(1, 1000001):
    check[i ** 3] = i
for test in range(1, t + 1):
    n = int(input())
    if n in check:
        print(f'#{test} {check[n]}')
    else:
        print(f'#{test} -1')