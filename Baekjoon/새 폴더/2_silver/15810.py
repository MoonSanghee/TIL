n, m = map(int, input().split())
staffs = list(map(int, input().split()))
# 스태프의 수와 풍선의 수 스태프가 풍선을 만드는데 필요한 시간을 받아줍니다.
s, e = 0, min(staffs) * m
# 0부터 풍선을 만드는데 가장 오래 걸리는 사람이 m 개의 풍선을 만드는데 걸리는 시간을 범위로 설정해줍니다.
while s <= e:
    mid = (s + e) // 2
    balloon = 0
    for i in range(n):
        balloon += mid // staffs[i]
    
    if balloon < m:
        s = mid + 1
    elif balloon >= m:
        e = mid - 1
# 이분탐색을 통해 시간을 구해줍니다.
print(s)
# 결과를 출력해줍니다.