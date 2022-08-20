import sys
sys.stdin = open('1860_input.txt', 'r')

test_case = int(input())

for test in range(1, test_case + 1):
    n, m, k = list(map(int, input().split()))
    people = list(map(int, input(). split()))
    people = sorted(people)
    boong = 0
    time = 0
    for i in range(n):
        time = people[i]
        boong = (time // m) * k
        boong -= (i + 1)
        if boong < 0:
            print(f'#{test} Impossible')
            break
    else:
        print(f'#{test} Possible')
# 대소문자 유의!!