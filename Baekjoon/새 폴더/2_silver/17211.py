n, now = map(int, input().split())
arr = list(map(float, input().split()))
# 주어지는 날의 수와 최초의 상태, 기분 변화 확률들을 받아줍니다
good = 0
bad = 0
if now == 0:
    good = 1
else:
    bad = 1
# 최초 기분을 표시해줍니다
for i in range(n):
    previous = good
    good = good * arr[0] + bad * arr[2]
    bad = previous * arr[1] + bad * arr[3]
# 기분 변화를 적용해줍니다
print(int(good * 1000))
print(int(bad * 1000))
# 각 확률을 1000씩 곱하여 정수부분까지 기분이 좋을 확률과 나쁠 확률을 차례대로 출력해줍니다