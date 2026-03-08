n = int(input())
T = list(map(int, input().split()))
# 주어지는 변수들을 받아줍니다
total = sum(T) + 8 * (n - 1)
# 전체 소요 시간을 구해줍니다
print(total // 24, total % 24)
# 결과를 출력해줍니다