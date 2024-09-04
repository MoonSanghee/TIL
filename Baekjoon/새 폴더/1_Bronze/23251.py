import sys
input = sys.stdin.readline
t = int(input())
# 테스트 케이스의 수를 받아줍니다.
for tc in range(t):
    print(23 * int(input()))
    # 23의 합으로 이루어진 수들도 포함하므로 23의 배수중 n번째 수를 출력해줍니다.