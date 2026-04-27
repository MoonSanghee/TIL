R, C, N = map(int, input().split())
# 주어지는 영역의 크기와 CCTV의 커버범위를 받아줍니다
if R % N:
    R //= N
    R += 1
else:
    R //= N

if C % N:
    C //= N
    C += 1
else:
    C //= N
# 가로, 세로를 커버하기 위한 CCTV가 얼마나 필요한지 받아줍니다
print(R * C)
# 두 값을 곱하여 출력해줍니다