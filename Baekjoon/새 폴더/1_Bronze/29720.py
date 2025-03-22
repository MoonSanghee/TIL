n, m, k = map(int, input().split())
minimum = max(n - (m * k), 0)
maximum = n - m * (k - 1) - 1
print(minimum, maximum)
# 주어지는 변수들을 받고 최소, 최댓값을 구하여 출력해줍니다