# SWEA 1860
t = int(input())
for test in range(1, t + 1):
    n, m, k = map(int, input().split())
    customer = list(map(int, input().split()))
    poss = 0
    customer.sort()
    for i in range(n):
        if (customer[i] // m) * k < i + 1:
            poss = 1
    if poss == 0:
        print(f'#{test} Possible')
    else:
        print(f'#{test} Impossible')

# 각 손님이 나타내는 시간은 시간이 경과한 후에 온다는 의미가 아니라 각 손님의 도착 시간이다.
# 따라서 정렬을 통해서 손님이 오는 시간에 붕어빵이 그 손님의 차례까지 충분히 준비 되어있는지 확인이 필요하다.