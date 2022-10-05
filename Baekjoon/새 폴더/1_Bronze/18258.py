from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
q = deque()

for i in range(n):
    command = list(map(str, input().split()))
    if len(command) > 1:
        q.append(command[1])
    else:
        if command[0] == 'pop':
            if q:
                a = q.popleft()
                print(a)
            else:
                print(-1)
        elif command[0] == 'size':
            print(len(q))
        elif command[0] == 'empty':
            if q:
                print(0)
            else:
                print(1)
        elif command[0] == 'front':
            if q:
                print(q[0])
            else:
                print(-1)
        else:
            if q:
                print(q[-1])
            else:
                print(-1)