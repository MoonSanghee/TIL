import sys
input = sys.stdin.readline

n = int(input())
# 주어진 좌표의 개수를 받아줍니다.
a, b = map(int, input().split())
# 직사각형의 크기를 받아줍니다.
data = set()

for _ in range(n):
    data.add(tuple(map(int, input().split())))
# 좌표를 data라는 set형에 넣어줍니다.
cnt = 0
# 직사각형의 개수를 담을 변수를 설정해줍니다.
for x, y in data:
    if (x + a, y) in data and (x, y + b) in data and (x + a, y + b) in data:
        cnt += 1
    # data의 각 값에 대하여 직사각형이 존재할 수 있는지 확인하여줍니다.
print(cnt)
# 직사각형의 개수를 출력해줍니다.