import sys

sys.stdin = open("sample_input.txt", "r")

test_case = int(input())

for test in range(1, test_case + 1):
    N, M = map(int, input().split())
    seet = []
    stop = 0

    for i in range(N):
        line = input()
        seet.append(line)

    for i in range(N):
        for j in range(M - 1):
            if seet[i][j] == seet[i][j + 1] and seet[i][j] != '?':
                print(f'#{test} impossible')
                stop = 1
                break


    for i in range(N - 1):
        for j in range(M):
            if seet[i][j] == seet[i + 1][j] and seet[i][j] != '?':
                print(f'#{test} impossible')
                stop = 1
                break

    
    if stop == 0:
        print(f'#{test} possible')