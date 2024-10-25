n, l = map(int, input().split())
# 신호등의 개수와 이동 거리를 받아줍니다
answer = 0
last = 0
# 걸린 시간과 마지막 신호등의 위치를 담을 변수를 설정해줍니다.
for _ in range(n):
    d, r, g = map(int, input().split())
    # 신호등의 정보를 받아줍니다.
    answer += (d - last)
    last = d
    # 신호등까지 도착하는데 걸리는 시간을 더하고 마지막 신호등의 위치를 갱신해줍니다.
    need = answer % (r + g)
    if need <= r:
        answer += (r - need)
    # 신호가 빨간불인지 확인하고 빨간불이라면 필요한 시간을 더해줍니다.
answer += (l - last)
print(answer)
# 목적지와 마지막 신호등 사이의 거리만큼 걸리는 시간을 더하고 결과를 출력해줍니다.