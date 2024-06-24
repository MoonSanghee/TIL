n = int(input())
balls = list(map(int, input().split()))
balls.sort()
# 구슬의 개수와 구슬을 받고 구슬을 오름차순으로 정렬해줍니다.
result = (balls[-1] - balls[0]) * 2
print(result)
# 구슬의 가장 큰 값에서 가장 작은 값을 빼고 2를 곱한 값을 출력해줍니다.

# result = balls[-1] - balls[0]
# for i in range(n - 1):
#     result += balls[i + 1] - balls[i]
# 구슬을 오름차순 혹은 내림차순으로 정렬한다음 이으면가장 적은 비용으로 만들수있고 
# 각 실의 길이를 합한 값은 가장 작은 값에서 가장 큰값까지 길이와 같으므로 그 값을 2곱한 값을 출력하면 됩니다.