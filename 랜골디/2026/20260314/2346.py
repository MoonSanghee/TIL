from collections import deque

N = int(input())
numbers = list(map(int, input().split()))
# 풍선과 종이의 값을 받아줍니다
result = [1]
# 처음 터트릴 풍선을 넣어줍니다
balls = deque([i + 1 for i in range(N)])
# 풍선을 차례대로 덱에 넣어줍니다
while len(result) < N:
    move = numbers[result[-1] - 1]
    balls.remove(result[-1])
    if move > 0:
        for _ in range(move - 1):
            balls.append(balls.popleft())
    elif move < 0:
        for _ in range(abs(move)):
            balls.appendleft(balls.pop())
    result.append(balls[0])
    # 이동을 진행하여 다음 터트릴 풍선을 찾아줍니다
print(*result)
# 결과를 출력해줍니다