T = int(input())
for test_case in range(1, T+1):
    result = 0
    nums = list(map(int, input().split()))
    for i in nums:
        result += i
    print(f'#{test_case} {round(result / 10)}')