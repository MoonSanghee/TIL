test_case = int(input())
for test in range(1, test_case + 1):
    area, spray = map(int, input().split())
    times = area // (spray * 2 + 1)
    times_ = area % (spray * 2 + 1)
    if times_ == 0:
        print(f'#{test} {times}')
    else:
        print(f'#{test} {times + 1}')