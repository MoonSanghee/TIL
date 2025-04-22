n, t = map(int, input().split())
# 버스의 대수와 영식이가 터미널에 도착하는 시간을 받아줍니다
result = 1000001
# 버스를 탈 시간을 담을 변수를 설정해줍니다
for _ in range(n):
    s, l, c = map(int, input().split())
    for _ in range(c):
        if s >= t:
            result = min(result, s)
            break
        else:
            s += l
# 각 버스마다 영식이의 도착 이후에 출발하는 차가 있는지 있다면 가장 빠른 시간의 차 시간을 확인하여 갱신해줍니다
if result == 1000001:
    print(-1)
else:
    print(result - t)
# 영식이가 캠프에 갈 수 없다면 -1 갈 수 있다면 기다리는 시간을 출력해줍니다