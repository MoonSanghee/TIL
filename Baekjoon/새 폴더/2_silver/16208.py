n = int(input())
sticks = list(map(int, input().split()))
# 막대의 개수와 필요한 각 막대의 길이를 받아줍니다
total = sum(sticks)
result = 0
# 막대 길이의 합을 구하고 비용을 담을 변수를 구해줍니다.
for i in range(n - 1):
    total -= sticks[i]
    result += total * sticks[i]
    # 각 막대를 자르는데 필요한 비용을 result에 더해줍니다.

print(result)
# 결과값을 출력해줍니다.