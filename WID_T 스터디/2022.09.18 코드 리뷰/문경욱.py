# SWEA 1216
import sys

sys.stdin = open("1216_input.txt", "r")

for t in range(1, 11):
    test = int(input())
    maps = []
    for i in range(100):
        maps.append(list(map(str, input())))
    length = 1
    for i in range(100):
        for j in range(100):
            for k in range(length, 101):
                if j + k > 100:
                    break
                if maps[i][j:j + k] == maps[i][j:j + k][::-1]:
                    length = k
                    continue

    maps2 = []
    for i in range(100):
        line = []
        for j in range(100):
            line.append(maps[j][i])
        maps2.append(line)
        
    for i in range(100):
        for j in range(100):
            for k in range(length, 101):
                if j + k > 100:
                    break
                if maps2[i][j:j + k] == maps2[i][j:j + k][::-1]:
                    length = k
                    continue

    print(f'#{test} {length}')

