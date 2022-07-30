import sys

sys.stdin = open("1979_input.txt", "r")

test_case =int(input())

for test in range(1, test_case + 1):
    a, b = map(int, input().split())

    chart = []
    for line in range(a):
        each_l = list(map(int, input().split()))
        chart.append(each_l)


    count = 0
    word_l = []

    for i in range(a):
        for j in range(a):
            if chart[i][j] == 1:
                count += 1
            else:
                word_l.append(count)
                count = 0
        word_l.append(count)
        count = 0



    for i in range(a):
        for j in range(a):
            if chart[j][i] == 1:
                count += 1
            else:
                word_l.append(count)
                count = 0
        word_l.append(count)
        count = 0
        

    result = word_l.count(b)

    print(f'#{test} {result}')