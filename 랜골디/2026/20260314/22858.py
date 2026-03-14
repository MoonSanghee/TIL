import sys
input = sys.stdin.readline

N, K = map(int, input().split())
S = list(map(int, input().split()))
D = list(map(int, input().split()))
# 주어지는 변수들을 받아줍니다
for _ in range(K):
    new = [0] * N
    for i in range(N):
        new[D[i] - 1] = S[i]

    S = new
# 셔플을 역으로 실행허여줍니다
print(*S)
# P를 출력해줍니다