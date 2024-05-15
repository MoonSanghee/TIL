n = int(input())
# 찾고자하는 수의 차례를 받아줍니다.
cnt = 1
mother = 1
son = 1
# 확인한 차례를 담을 변수와 분모, 분자값을 담을 변수를 설정해줍니다.
while True:
    if cnt == n:
        break
    # 목표로하는 차례에 도달하면 멈추어줍니다.
    if mother == 1:
        mother = son + 1
        son = 1
    else:
        mother -= 1
        son += 1
    cnt += 1
    # 원하는 차례에 도달하지 못하였다면 분모, 분자값을 변경하고 차례를 갱신해줍니다.

print(mother, son)
# 분모, 분자값을 차례대로 출력해줍니다.