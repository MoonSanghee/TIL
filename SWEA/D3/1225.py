cycle = [1, 2, 3, 4, 5]

for test in range(1, 11):
    test_num = int(input())
    numbers = list(map(int, input().split()))

    cnt = 0
    while numbers[-1] > 0:
        numbers[0] -= cycle[cnt % 5]
        cnt += 1
        numbers = numbers[1::] + [numbers[0]]
    numbers[-1] = 0

    print(f'#{test}', end = ' ')
    for i in numbers:
        print(i, end = ' ')
    print()