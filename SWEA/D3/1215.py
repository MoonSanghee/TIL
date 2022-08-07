import sys

sys.stdin = open("1215_input.txt", "r")

test_case = 10
for test in range(1, test_case + 1):
    num = int(input())
    
    seet = []
    cnt = 0
    for _ in range(8):
        line = list(input())
        seet.append(line)

    for i in range(8):
        for j in range(9 - num):
            word = ''
            for k in range(num):
                word += seet[i][j + k]
            if word == word[::-1]:
                cnt += 1

        for j in range(9 - num):
            word = ''
            for k in range(num):
                word += seet[j + k][i]
            if word == word[::-1]:
                cnt += 1
    print(f'#{test} {cnt}')