from collections import deque
maps = dict()
for i in range(5):
    line = (list(map(int, input().split())))
    for j in range(5):
        maps[line[j]] = (i, j)
        
check = deque()
for i in range(5):
    line = (list(map(int, input().split())))
    for j in line:
        check.append(j)
call = check.popleft()
cnt = 0
bingo = 0
for i in range(5):
    for j in range(5):
        if maps[i][j] == call:
            maps[i][j] = 0
            cnt += 1
        
