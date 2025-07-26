N, Q = map(int, input().split())
arr = list(map(int, input().split()))
Qi = list(map(int, input().split()))
# 주어지는 소의 수와 장난치는 횟수
# 소의 등급과 장난칠 소의 번호를 받아줍니다
result = sum(arr[i] * arr[(i + 1) % N] * arr[(i + 2) % N] * arr[(i + 3) % N] for i in range(N))
# 최초의 계산 합을 구해줍니다
for i in Qi:
    arr[i - 1] *= -1
    for j in range(i - 4, i):
        result += 2 * arr[j] * arr[(j + 1) % N] * arr[(j + 2) % N] * arr[(j + 3) % N]
    print(result)
    # 장난친 소의 번호를 받고 영향을 받는 범위의 곱을 수정한 값을 더해 바뀐 결과를 출력해줍니다