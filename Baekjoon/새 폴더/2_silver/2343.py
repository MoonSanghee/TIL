n, m = map(int, input().split())
minutes = list(map(int, input().split()))
# 녹음할 영상의 개수와 각 영상의 길이 그리고 나눠 담을 블루레이의 개수를 받아줍니다.
l, r = min(minutes), sum(minutes)
# 찾을 범위 l과 r을 정해줍니다.
while l <= r:
    mid = (l + r) // 2
    now = mid
    cnt = 1
    # 범위가 유효할때 확인할 mid값을 찾고 몇 개의 블루레이에 담겼는지 저장할 cnt를 만들어줍니다.
    for i in minutes:
        if now < i:
            now = mid
            cnt += 1
        now -= i
        # 남은 시간이 부족하면 블루레이를 하나 추가해주며 몇 개의 블루레이에 나눠 담았는지 확인해줍니다.
    
    if cnt > m or mid < max(minutes):
        l = mid + 1
    else:
        r = mid - 1
        target = mid
        # cnt와 mid 값을 확인하며 범위를 조정해줍니다.

print(target)
# 필요한 블루레이의 최소 길이를 출력해줍니다.