t,n = map(int, input().split())
# 필요한 수면시간과 수면 횟수를 받아줍니다.
days = ["Mon","Tue","Wed","Thu","Fri"]
# 월요일부터 금요일까지 리스트에 차례대로 담아둡니다.
for _ in range(n):
    d1, h1, d2, h2 = input().split()
    # 자는 날의 정보와 일어나는 날의 정보를 받아줍니다.
    if d1 == d2:
        t -= int(h2) - int(h1)
    # 잠에 든 날에 일어난다면 시간의 차이를 비교하여 필요한 수면 시간을 갱신해줍니다.
    else:
        t -= 24 * (days.index(d2) - days.index(d1)) + int(h2) - int(h1)
    # 잠에 든 날과 일어난 날이 다르다면 며칠을 잤는지 확인하고 필요한 수면 시간을 갱신해줍니다.
if t > 48:
    print(-1)
elif t > 0:
    print(t)
elif t > -49:
    print(0)
# 필요한 수면 시간에 맞게 결과를 출력해줍니다.