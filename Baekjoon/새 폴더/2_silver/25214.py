n = int(input())
A = list(map(int, input().split()))
# 수의 개수와 수열을 받아줍니다
N = [0] * n
minimum = A[0]
# 각 수를 추가할때마다 구할수있는 최대값을 담을 변수와 수열의 최소값을 담을 변수를 설정해줍니다
for i in range(1, n):
    N[i] = max(N[i - 1], A[i] - minimum)
    minimum = min(minimum, A[i])
    # 수열을 순회하며 각 수가 추가될때 Aj - Ai의 최댓값을 구하고 수열의 최소값을 갱신해줍니다

print(*N)
# 결과를 출력해줍니다