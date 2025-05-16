import math

n, k = map(int, input().split())
d = dict()
# 주어지는 학생수와 방에 배정할 수있는 최대 인원을 받아줍니다
for _ in range(n):
    s, y = map(int, input().split())
    # 학년과 성별을 받아줍니다
    if y % 2 == 0:
        y -= 1
    # 1,2학년, 3,4학년, 5,6학년 끼리는 같은 방을 쓸 수 있으니 짝수 학년이라면 1씩 빼줍니다
    if y == 1:
        s = 0
    # 1,2학년은 성별에 상관없이 방을 같이 쓸 수 있으므로 하나의 성별로 맞추어줍니다
    d[(s, y)] = d.get((s, y), 0) + 1
    # 기준에 따라 학생을 나누어줍니다
rooms = 0
for i in d:
    rooms += math.ceil(d[i] / k)
# 기준에 따라 각각 몇개씩의 방이 필요한지 확인해줍니다
print(rooms)
# 결과를 출력해줍니다