import sys
import heapq
input = sys.stdin.readline
# 프림 알고리즘을 이용한 풀이
N = int(input())
M = int(input())

eList = [[] for _ in range(N )]

for _ in range(M):
    a, b, c = map(int, input().split())
    eList[a - 1].append((c, b - 1))
    eList[b - 1].append((c, a - 1))

heap = [[0, 0]]
visited = [False] * (N)

result = 0
cnt = 0

while heap:
    if cnt == N:
        break
    distance, end = heapq.heappop(heap)
    if not visited[end]:
        visited[end] = True
        result += distance
        cnt += 1
        for i in eList[end]:
            heapq.heappush(heap, i)

print(result)