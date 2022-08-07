import sys

sys.stdin = open("1220_input.txt", "r")


for test in range(1, 11):
    length = int(input())
    metrix = [list(map(int, input().split())) for _ in range(100)]
    cnt = 0
    for i in range(length):
        left = []
        for j in range(length):
            if metrix[j][i] == 1:
                left.append(metrix[j][i])
            if metrix[j][i] == 2:
                if len(left) > 0:
                    left.append(metrix[j][i])
        if len(set(left)) == 1:
            left = []
        for j in range(len(left) - 1):
            if left[j] == 1 and left[j + 1] == 2:
                cnt +=1
    print(f'#{test} {cnt}')