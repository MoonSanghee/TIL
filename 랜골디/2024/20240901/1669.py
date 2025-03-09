monkey, dog = map(int, input().split())
need = dog - monkey
# 원숭이와 개의 크기를 받고 차이를 확인해줍니다.
limit = 0
day = 0
# 각 날별로 클수있는 제한 키와 필요한 날을 담을 변수를 설정해줍니다.
while True:
    if need <= limit:
        print(day)
        break
    # 키 차이가 제한보다 작아지면 현재 날짜안에 도달할수있으므로
    # 값을 출력하고 작동을 멈추어줍니다.
    limit += (day // 2) + 1
    day += 1
    # 각 날짜에 클수있는 최대 클수있는 제한 키까지 컸다고 계산하고 날짜를 갱신해줍니다.