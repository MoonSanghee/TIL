import sys
from collections import deque

input = sys.stdin.readline

# 명령의 개수를 받아줍니다.
n = int(input())
# 덱 자료구조를 만들어줍니다.
q = deque()
# 각 주어지는 명령에 따라 알맞을 결과를 출력시켜줍니다
for _ in range(n):
    commands = list(map(int, input().split()))
    if commands[0] == 1:
        q.appendleft(commands[1])
    elif commands[0] == 2:
        q.append(commands[1])
    elif commands[0] == 3:
        if q:
            x = q.popleft()
            print(x)
        else:
            print(-1)
    elif commands[0] == 4:
        if q:
            x = q.pop()
            print(x)
        else:
            print(-1)
    elif commands[0] == 5:
        print(len(q))
    elif commands[0] == 6:
        if q:
            print(0)
        else:
            print(1)
    elif commands[0] == 7:
        if q:
            x = q.popleft()
            print(x)
            q.appendleft(x)
        else:
            print(-1)
    elif commands[0] == 8:
        if q:
            x = q.pop()
            print(x)
            q.append(x)
        else:
            print(-1)