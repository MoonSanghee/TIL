import sys
input = sys.stdin.readline
n = int(input())
numbers = list(map(int, input().split()))
# 수의 개수와 수열을 받아줍니다.

new = [0]
result = 0

for i in numbers:
    result += i
    new.append(result)
# 각 자리까지 누적합을 구하여줍니다.

t = int(input())
for tc in range(t):
    s, e = map(int, input().split())
    print(new[e] - new[s - 1])
    # 원하는 범위의 마지막 수까지 합에서 시작 점까지 합을 빼준 값을 출력해줍니다.