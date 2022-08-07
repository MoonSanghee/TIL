test_case = int(input())

for test in range(1, test_case + 1):
    line = input()
    count_x = line.count('x')

    if count_x > 7:
        print(f'#{test} NO')
    else:
        print(f'#{test} YES')