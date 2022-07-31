import sys

sys.stdin = open("1209_input.txt", "r")

test_case = 10

for test_num in range(1, test_case + 1):
    
    test_num = int(input())

    seet = []

    for i in range(100):
        line = list(map(int, input().split()))
        seet.append(line)

    sum_nums = []
    cross1 = 0
    cross2 = 0
    for i in range(100):
        sum_nums.append(sum(seet[i]))
        
        vertical = []
        for j in range(100):
            vertical.append(seet[j][i])
        sum_nums.append(sum(vertical))

        cross1 += seet[i][i]
        cross2 += seet[i][99 - i]

    sum_nums.append(cross1)
    sum_nums.append(cross2)

    print(f'#{test_num} {max(sum_nums)}')