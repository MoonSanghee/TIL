n = int(input())
statue = list(map(int, input().split()))
# 석상의 개수와 석상의 배치를 입력받습니다.
l = 0
r = 0
long = 0
# 왼 쪽으로 얼마나 길게 서있는지와 오른쪽으로 얼마나 길게 서있는지 
# 그리고 최장 길이를 확인해줍니다.
for i in statue:
    if i == 1:
        l += 1
        r -= 1
    else:
        r += 1
        l -= 1
    # 석상이 1이면 l을 1더하고 r을 1빼고 2라면 반대로 계산해줍니다.
    if l <= 0:
        l = 0
    elif r <= 0:
        r = 0
    # l이나 r이 0보다 작은경우 0으로 바꾸어줍니다.
    long = max(long, l, r)
    # 매번 최장거리가 갱신되었는지 확인하여줍니다.

print(long)
# 가장 긴 길이가 얼마인지 출력해줍니다.