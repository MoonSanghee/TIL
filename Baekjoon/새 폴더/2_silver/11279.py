import heapq, sys
input = sys.stdin.readline
n = int(input())
li = []
for i in range(n):
    a = int(input())
    if a == 0:
        if li:
            print(-heapq.heappop(li))
        else:
            print(0)
    else:
        heapq.heappush(li, -a)