import sys
input = sys.stdin.readline
n, x = map(int, input().split())
# 주어지는 높이와 구르면서 커지는 배수를 받아줍니다
result = 0
now = 1
# 결과와 현재 높이에서 크기를 받아줍니다
for i in range(n):
    number = int(input())
    now *= x
    now %= (10 ** 9 + 7)
    # 높이가 1만큼 지났으므로 크기를 증가시켜줍니다
    result += number * now
    result %= (10 ** 9 + 7)
    # 결과값에 주어진 공의 개수만큼 크기를 더해줍니다
print(result)
# 결과를 출력해줍니다