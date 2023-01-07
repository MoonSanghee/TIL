from collections import deque

s, t = map(int, input().split())
# 시작하는 숫자와 원하는 숫자를 입력해줍니다.
q = deque()
visited = set()
# 방문값을 저장해줄 set()을 만들어줍니다.
if s == t:
    print(0)
    # 두 수가 같다면 연산할 필요가 없으니 1을 출력해 줍니다.
elif t == 1:
    print('/')
    # t가 1일 경우 나누기를 1번 실행하면 되므로 1을 나누어줍니다.
else:
    q.append([s, ''])
    # 시작하는 수와 연산을 안 한 상태를 q에 넣어주고 시작수를 방문처리합니다.
    visited.add(s)
    while q:
        x, y = q.popleft()
        if x == t:
            print(y)
            break
        # 꺼냈을때 원하는 값이라면 연산을 출력해주고 아니라면
        else:
            if x ** 2 <= 10**9 and x**2 not in visited:
                visited.add(x**2)
                q.append([x**2, y+'*'])
            if x * 2 <= 10**9 and x*2 not in visited:
                visited.add(x*2)
                q.append([x*2, y+'+'])
            if x / x not in visited:
                visited.add(1)
                q.append([1, y+'/'])
        # 10**9 이하의 수중에 연산이 가능한지 확인해줍니다.
    else:
        print(-1)
        # 적합한 연산이 없을 경우 -1을 출력해줍니다.