import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
q = deque()
# 덱 자료형 만들어줍니다.
for i in range(n):
    command = list(input().split())
    if command[0] == 'push_back':
        q.append(command[1])
    elif command[0] == 'push_front':
        q.appendleft(command[1])
    # push_back은 뒤에 오는 것이니 그냥 append를
    # push_front는 앞에 오는 것이니 appendleft를 이용하여 값을 넣어줍니다.
    elif command[0] == 'pop_front':
        if not q:
            print(-1)
        else:
            print(q.popleft())
    elif command[0] == 'pop_back':
        if not q:
            print(-1)
        else:
            print(q.pop())
    # pop의 경우 두 경우 다 값이 없다면 -1을 출력해주고 값이 있다면
    # pop_front는 앞의 값을 빼주고
    # pop_back은 뒤의 값을 빼 출력해줍니다.
    elif command[0] == 'size':
        print(len(q))
    # size는 남아있는 정수가 몇개인지 출력해주고
    elif command[0] == 'empty':
        if q:
            print(0)
        else:
            print(1)
    # empty는 비었는지 유무를 확인해 출력해줍니다.
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
    # 마지막으로 front와 back은 덱이 비었는지 확인해서 비어있지 않다면
    # 물어본 위치의 값을 출력해줍니다.