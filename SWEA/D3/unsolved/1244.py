import sys
sys.stdin = open('1244_input.txt', 'r')

test_case = int(input())
for test in range(1, test_case + 1):
    num, change = map(str, input().split())
    change = int(change)
    num_l = []
    for i in range(len(num)):
        num_l.append(int(num[i]))
    cnt = change
    num_r = num_l[::-1]
    for i in range(change):
        for j in range(len(num_l) - 1):
            if num_l[j] < max(num_l[j + 1::]):
                m = max(num_l[j + 1::])
                num_l[(num_r.index(m) + 1) * -1], num_l[j] = num_l[j], num_l[(num_r.index(m) + 1) * -1]
                num_r = num_l[::-1]
                cnt -= 1
                break

    number = ''
    for i in range(len(num_l)):
        number += str(num_l[i])
    print(f'#{test} {number}')
# num = int(num)