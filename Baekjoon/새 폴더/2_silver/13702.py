n, k = map(int, input().split())
bottles = [int(input()) for _ in range(n)]
# 사람과 병의 수를 받고 병의 용량을 받아줍니다.
start, end = 1, max(bottles)
answer = 0
# 범위의 최소값과 최대값 범위를 설정해주고 답을 답을 변수를 설정합니다.

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    # 중앙값을 확인해주고 몇 병이 나오는지 담을 값을 설정해줍니다.
    for i in bottles:
        cnt += (i // mid)
    # 각 병을 순회하며 몇 명이 나눌수있는지 확인해줍니다.

    if cnt >= k:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1
        # 몇명이 누눌수있는지 확인하고 범위를 수정해줍니다.

print(answer)
# answer에 담긴 값을 출력해줍니다.