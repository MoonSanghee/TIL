import sys
from collections import deque
input = sys.stdin.readline
t = int(input())
# 테스트 케이스가 몇개인지 받아줍니다
for _ in range(t):
    a, b = map(int, input().split())
    # 주어지는 초기값과 결과값을 받아줍니다
    used = [False for _ in range(10001)]
    used[int(a)] = True
    # 도달했던 숫자를 확인할 방문리스트를 만들고 초기값을 방문처리해줍니다
    q = deque()
    q.append((a, ''))
    # 큐를 만들고 초기값과 아무런 입력이 없었다는 의미로 공백을 문자열로 묶어 넣어줍니다
    while True:
        x, y = q.popleft()
        # 큐에서 가장 왼쪽값을 뽑아 값과 입력을 받아줍니다
        if x == b:
            print(y)
            break
        # 값이 결과값과 동일하다면 반복을 멈추어줍니다
        d = ((int(x) * 2) % 10000)
        if used[d] == False:
            used[d] = True
            q.append((d, y + 'D'))
        s = ((int(x) - 1) % 10000)
        if used[s] == False:
            used[s] = True
            q.append((s, y + 'S'))
        l = (int(x) // 1000 + (int(x) % 1000) * 10)
        if used[l] == False:
            used[l] = True
            q.append((l, y + 'L'))
        r = (int(x) // 10 + (int(x) % 10) * 1000)
        if used[r] == False:
            used[r] = True
            q.append((r, y + 'R'))
        # 주어진 DSLR을 실행한 결과를 구하여 각 값에 도달한 적 없다면 실행 명령을 추가한 값을 연산값과 묶어 큐에 넣어줍니다