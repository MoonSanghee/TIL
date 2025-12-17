cnt = 0
# 피자의 번호를 담을 변수를 설정해줍니다
while True:
    cnt += 1
    numbers = list(map(int, input().split()))
    # 피자번호를 갱신하고 주어지는 피자와 식탁의 정보를 받아줍니다
    if numbers[0] == 0:
        break
    if (numbers[0] * 2) ** 2 >= numbers[1] ** 2 + numbers[2] ** 2:
        print(f"Pizza {cnt} fits on the table.")
    else:
        print(f"Pizza {cnt} does not fit on the table.")
    # 피자가 놓아지는지 확인하여 주어진 형식에 맞게 출력해줍니다