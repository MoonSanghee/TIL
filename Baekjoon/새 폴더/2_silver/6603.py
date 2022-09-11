from collections import deque

def bfs():
    q = deque()
    for i in range(1, numbers[0] - 4):
        q.append((i, [numbers[i]]))
    while q:
        idx, combi = q.popleft()
        if len(combi) == 6:
            for i in range(6):
                print(combi[i], end = ' ')
            print()
        for i in range(idx + 1, numbers[0] + 1):
            if len(combi) <= 6:
                q.append((i, combi + [numbers[i]]))

while True:
    numbers = list(map(int, input().split()))
    if numbers == [0]:
        break
    else:
        bfs()
        print()

# 찾아본 코드 1 콤비네이션 함수 호출
# from itertools import combinations

# while True:
#     s = list(map(int, input().split()))
#     if s[0] == 0:
#         break
#     del s[0]
#     s = list(combinations(s, 6))
#     for i in s:
#         for j in i:
#             print(j, end=' ')
#         print()
#     print()

# 찾아본 코드2 dfs 백트래킹
# def dfs(start, depth):
#     if depth == 6:
#         for i in range(6):
#             print(combi[i], end=' ')
#         print()
#         return
#     for i in range(start, len(s)):
#         combi[depth] = s[i]
#         dfs(i + 1, depth + 1)
# combi = [0 for i in range(13)]
# while True:
#     s = list(map(int, input().split()))
#     if s[0] == 0:
#         break
#     del s[0]
#     dfs(0, 0)
#     print()