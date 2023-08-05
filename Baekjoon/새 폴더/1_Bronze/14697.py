from collections import deque
A, B, C, N = map(int, input().split())
# 세 방의 규격과 사람을 받아줍니다.
q = deque()
# q를 덱 형식으로 받아줍니다.
q.append(0)
# q에 0을 넣어줍니다.
rooms = [0 for _ in range(N + 1)]
# N명까지 딱맞게 들어가는지 확인해 표시할 리스트를 만들어줍니다.
rooms[0] = 1
# 첫번째 인덱스를 1로 바꾸어줍니다.0
while q:
    # q에 값이 없을때까지 반복하여줍니다.
    x = q.popleft()
    # q의 가장 앞의 값을 빼서
    for i in [x + A, x + B, x + C]:
        if i <= N and rooms[i] == 0:
            # 3방의 크기만큼 인원이 더 증가한 경우를 확인하지 않았고 N이하라면
            rooms[i] = 1
            q.append(i)
            # rooms[i]를 1로 바꾸고 q에 i를 널어줍니다.

print(rooms[-1])
# N명이 남지않고 딱 분배가능한지 확인하여 출력해줍니다.