import sys
import heapq
input = sys.stdin.readline

n = int(input())
nums = []
for i in range(n):
    heapq.heappush(nums, float(input()))

for i in range(7):
    n = heapq.heappop(nums)
    print(f'{n:.3f}')
    # 힙을 이용하여 풀었음.
    # 포멧을 이용하여 소수점 특정 자리까지 표현 해주는법을 다시 찾아봄.