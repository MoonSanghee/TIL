from collections import deque
n, k = map(int, input().split())
maps = [0 for _ in range(100001)]
# 출발점과 도착점을 받고 전체 갈 수 있는 위치를 표시할 리스트를 만들어 줍니다.
def check(a):
    q = deque()
    q.append(a)
    cnt = 0
    # 목표점에 최소 시간을 소모하며 도착할 수 있는 가짓수를 입력해줄 변수입니다.
    while q:
        x = q.popleft()
        if x == k:
            cnt += 1
            # 나온 값이 희망 도착지점과 같으면 도착 횟수를 1회 추가하여줍니다.
        for i in [x - 1, x + 1, 2 * x]:
            if i in range(100001):
                if maps[i] == 0 or maps[i] >= maps[x] + 1:
                    maps[i] = maps[x] + 1
                    q.append(i)
                    # 위치에 처음 오거나 입력되어있는 값이 지금 도달했을때 걸릴 시간보다 크다면 생긴해주고
                    # 위치를 q에 넣어줍니다.
    return cnt
    # 확인한 횟수를 반환합니다.
if n == k:
    print(0)
    print(1)
    # 출발과 목표점이 같다면 시간은 0, 방법은 1을 출력해줍니다.
else:
    result = check(n)
    print(maps[k])
    print(result)
    # 이외의 경우 만들어준 함수를 사용하여 k위치에 저장된 걸린 시간되 반환받은 cnt값을 출력해줍니다.