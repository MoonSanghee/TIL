# 백준 1715
import heapq
n = int(input())
numbers = []
for i in range(n):
    heapq.heappush(numbers, int(input()))

if len(numbers) == 1:
    print(0)
else: 
    result = 0
    while len(numbers) > 1:
        deck = heapq.heappop(numbers)
        deck2 = heapq.heappop(numbers)
        result += deck + deck2
        heapq.heappush(numbers, deck + deck2)
    print(result)