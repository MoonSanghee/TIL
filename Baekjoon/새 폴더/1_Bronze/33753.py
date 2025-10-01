a, b, c = map(int, input().split())
t = int(input())
# 주어지는 변수를 받아줍니다
if t < 30:
    print(a)
    # 30분 미만이라면 기본요금을 출력해줍니다
else:
    t -= 30
    if t % b == 0:
        print(a + ((t // b) * c))
    else:
        print(a + ((t // b + 1) * c))
    # 30분을 초과하면 추가 시간만큼 요금을 계산하여 출력해줍니다