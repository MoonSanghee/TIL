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
        deck1 = heapq.heappop(numbers)
        deck2 = heapq.heappop(numbers)
        result += deck1 + deck2
        heapq.heappush(numbers, deck1 + deck2)
    print(result)

# 나의 풀이 (오답)
# n = int(input())
# numbers = []
# for i in range(n):
#     num = int(input())
#     numbers.append(num)
# numbers = sorted(numbers, reverse = True)
# result = 0
# while len(numbers) != 1:
#     x = numbers.pop()
#     y = numbers.pop()
#     numbers.append(x + y)
#     result += x + y

# print(result)
# result 값이 가장 뒤에 오는것이 확정이 아니라 result 값을 포함한 리스트에서 또다시 가장 작은 값 둘을 뺴주어야한다.
# 그러므로 리스트에서 정렬을 반복하는 방식이 아닌 heapq를 사용해주어야 한다.