from collections import deque
n, k = input().split()
# 수와 교환을 몇 번 할것인지를 받아줍니다.
m = len(n)
k = int(k)
# 교환 횟수는 정수형으로 바꿔줍니다.

def bfs(a, b):
    q = deque()
    q.append((a, 0))
    visited = set()
    visited.add((a, 0))
    # 덱에 문자열 형태의 받은 수와 0번 교환했다는 것을 넣고
    # set형태로 방문 확인을 위한 visited를 만들어 같은 덱과 같은 값을 넣어줍니다.
    num = 0
    # 교환 결과 가장 큰 값을 비교해줄 변수를 정해줍니다.
    while q:
        now, cnt = q.popleft()
        # 덱에서 뺀 값을 수를 현재 형태 cnt를 교환횟수로 받아줍니다.

        if cnt == b:
            num = max(num, int(now))
            continue
        # cnt가 목표 횟수에 도달했다면 정수로 변환하여 num과 크기를 비교해줍니다.

        x = list(now)
        # num을 리스트 형태로 바꾸어 변수에 담아줍니다.

        for i in range(m):
            for j in range(i + 1, m):
                if i == 0 and x[j] == '0':
                    continue
                # x의 2자리를 비교하여 맨 앞에 0이 오는 경우라면 교환을 하지않고
                x[i], x[j] = x[j], x[i]
                new = ''.join(x)
                if (new, cnt + 1) not in visited:
                    q.append((new, cnt + 1))
                    visited.add((new, cnt + 1))
                x[i], x[j] = x[j], x[i]
                # 아니라면 두 자리를 교환한 다음 합친 문자를 new로 만들고
                # new와 cnt + 1의 튜플이 나온적 없다면 덱과 visited에 추가해줍니다.
    return num
    # num에 저장된 값을 반환합니다.

result = bfs(n, k)
if result:
    print(result)
else:
    print(-1)
# bfs를 시행한 값이 0이라면 교환이 일어나지 못한것이므로 -1을 출력해주고
# 아니라면 시행 결과를 출력해줍니다.