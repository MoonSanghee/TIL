A, B, N = map(int, input().split())
# 주어지는 변수들을 받아줍니다
result = [A * N + (B * (i + 1)) for i in range(N)]
# B가 드러나는 정도에따라 높이가 달라지므로 N개의 경우를 구해줍니다
print(*result)
# 결과를 주어진 형식대로 출력해줍니다