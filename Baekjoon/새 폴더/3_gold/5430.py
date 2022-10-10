# import sys
# input = sys.stdin.readline
from collections import deque

tc = int(input())
for t in range(tc):
    commands = input().rstrip()
    length = int(input())
    li = list(input()[1:-1].split(','))
    r = 0
    error = 0
    q = deque()
    for i in range(length):
        q.append(li[i])
    for i in commands:
        if i == 'R':
            r += 1
        elif i =='D':
            if q:
                if r % 2:
                    q.pop()
                else:
                    q.popleft()
            else:
                error = 1
    if error == 1:
        print('error')
    else:
        if r % 2:
            print('[',end='')
            for i in range(len(q) - 1, -1 ,-1):
                if i == 0:
                    print(q[i], end='')
                else:
                    print(q[i], end=',')
            print(']')
            
        else:
            print('[',end='')
            for i in range(len(q)):
                if i == len(q) - 1:
                    print(q[i], end='')
                else:
                    print(q[i], end=',')
            print(']')