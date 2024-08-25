n = int(input())
# 식단의 길이를 받아줍니다.
s = input()
cnt = s.count('C')
# 식단을 받고 치킨을 먹는날이 총 며칠인지 확인해줍니다.
if cnt == 0:
    print(0)
else:
    print(n // (n - cnt + 1))
# 치킨을 먹는날이 없으면 0 아니면 최소한으로 먹을수 있는날을 출력해줍니다.