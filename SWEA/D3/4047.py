import sys
sys.stdin = open('sample_input.txt')

test = int(input())
for t in range(1, test + 1):
    sen = list(map(str, input()))
    check = []
    for i in range(13):
        check.append([1, 1, 1, 1])
    patten = ['S', 'D', 'H', 'C']
    for i in range(0, len(sen), 3):
        if sen[i] in patten:
            check[int(sen[i + 1] + sen[i + 2]) - 1][patten.index(sen[i])] -= 1
            if check[int(sen[i + 1] + sen[i + 2]) - 1][patten.index(sen[i])] < 0:
                print(f'#{t} ERROR')
                # print(check)
                break
    else:
        cnts = []
        for j in range(4):
            cnt = 0
            for i in check:
                cnt += i[j]
            cnts.append(cnt)
        print(f'#{t}', end = ' ')
        print(*cnts)