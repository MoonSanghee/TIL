a1, a0 = map(int, input().split())
# a1, a0을 받아줍니다.
c = int(input())
n0 = int(input())
# c와 n0을 받아줍니다.
if (a1 * n0 + a0 <= c * n0) and (a1 <= c):
    print(1)
else:
    print(0)
# 주어진 조건에 적합한지 확인하여 1 또는 0을 출력해줍니다.