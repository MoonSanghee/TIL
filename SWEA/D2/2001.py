import sys

sys.stdin = open("2001_input.txt", "r")

test_case = int(input())

for test_num in range(1, test_case + 1):
    N, M = map(int, input().split())

    number_seet = []
    for line in range(N):
        each_line = list(map(int, input().split()))
        number_seet.append(each_line)
    
    best = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            m = 0
            for im in range(M):
                line_m = 0
                for jm in range(M):
                    line_m += number_seet[i + im][j + jm]
                m += line_m
            if m > best:
                best = m

    print(f'#{test_num} {best}')