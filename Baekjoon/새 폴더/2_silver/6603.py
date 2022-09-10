from collections import deque

def bfs():
    q = deque()
    for i in range(1, numbers[0] - 4):
        q.append((i, [numbers[i]]))
    while q:
        idx, combi = q.popleft()
        if len(combi) == 6:
            for i in range(6):
                print(combi[i], end = ' ')
            print()
        for i in range(idx + 1, numbers[0] + 1):
            if len(combi) <= 6:
                q.append((i, combi + [numbers[i]]))

while True:
    numbers = list(map(int, input().split()))
    if numbers == [0]:
        break
    else:
        bfs()
        print()
