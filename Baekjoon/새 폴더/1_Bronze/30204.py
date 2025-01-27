n, x = map(int, input().split())
result = sum(list(map(int, input().split())))
# 생활관의 수와 피자를 몇명이 나눠 먹는지를 받고 전체 인원을 받아줍니다.
if result % x == 0:
    print(1)
else:
    print(0)
# 전체 인원을 x로 나누어 떨어지면 모두 하나의 그룹에 속하므로 1 아니면 0을 출력해줍니다