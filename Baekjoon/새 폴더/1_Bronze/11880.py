import sys

input = sys.stdin.readline
t = int(input())
# 테스트 케이스의 수를 받아줍니다.
for tc in range(t):
    lines = list(map(int, input().split()))
    lines.sort()
    # 세 선의 길이를 받고 정렬시켜줍니다.
    print((lines[0] + lines[1]) ** 2 + lines[2] ** 2)
    # 짧은 두 선의 길이를 더해 제곱한 수와 긴 선의 제곱을 더한 값을 출력해줍니다.