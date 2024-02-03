now = list(map(int, input().split(':')))
start = list(map(int,input().split(':')))
# 현재 시간과 임무를 시작하는 시간을 받아줍니다.
nowSeconds = now[0] * 3600 + now[1] * 60 + now[2]
startSeconds = start[0] * 3600 + start[1] * 60 + start[2]

if nowSeconds > startSeconds:
    startSeconds += 24 * 3600
# 입력받은 시간을 초단위로 변환하여 차를 구해줍니다.
t = startSeconds - nowSeconds
h = t // 3600
m = (t % 3600) // 60
s = t % 60
print("%02d:%02d:%02d" % (h,m,s))
# 필요한 시간을 구하여 요청받은 형식대로 출력해줍니다.