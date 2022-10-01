import heapq, sys
input = sys.stdin.readline
n = int(input())
li = []
for _ in range(n):
    com = int(input())
    if com == 0:
        if li:
            print(heapq.heappop(li))
        else:
            print(0)
    else:
        heapq.heappush(li, com)
