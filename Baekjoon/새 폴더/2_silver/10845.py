import sys
input = sys.stdin.readline
n = int(input())
q = []
for _ in range(n):
    co = input().split()
    if co[0] == 'push':
        q.append(co[1])
    elif co[0] == 'pop':
        if q:
            print(q[0])
            q = q[1::]
        else:
            print(-1)
    elif co[0] == 'size':
        print(len(q))
    elif co[0] == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif co[0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    else:
        if q:
            print(q[-1])
        else:
            print(-1)