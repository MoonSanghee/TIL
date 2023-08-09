now = list(map(int, input().split(':')))
target = list(map(int, input().split(':')))
# 현재 시간과 폭죽을 터트릴 시간을 받아줍니다.
t1 = now[0] * 3600 + now[1] * 60 + now[2]
t2 = target[0] * 3600 + target[1] * 60 + target[2]
# 현재 시간과 폭죽을 터트릴 시간을 초로 변환하여줍니다.
if t1 > t2:
    wait = t2 - t1 + 24 * 3600
else:
    wait = t2 - t1
# 기다릴 시간을 계산해줍니다.

h = wait//60//60
m = wait//60 % 60
s = wait%60
# 시간, 분, 초단위로 나누어줍니다.
print("%02d:%02d:%02d" % (h, m, s))
# 주어진 형식에 맞게 출력하여줍니다.