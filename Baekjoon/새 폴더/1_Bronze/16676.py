n = int(input())
# 주어지는 수를 받아줍니다
if n == 0:
    print(1)
else:
    cnt = 1
    while True:
        if int(cnt * '1') > n:
            break
        cnt += 1

    print(cnt - 1)
    # 1, 11, 111과 같이 1이 한 개씩 더 필요할때마다 카드 한 더미가 더 필요합니다