n, m = map(int, input().split())
get = list(map(int, input().split()))
# 확인할 날의 수와 제한 스트레스를 받고 날마다 받게될 스트레스의 양을 받아줍니다
stress = 0
days = 0
# 누적 스트레스와 스트레스가 한계를 넘긴 날의수를 담을 변수를 설정해줍니다.
for i in get:
    stress += i
    # 스트레스를 더해줍니다.
    if stress < 0:
        stress = 0
    elif stress >= m:
        days += 1
    # 스트레스가 음수라면 0으로 설정해줍니다.
    # 스트레스가 제한을 넘겼다면 날을 더해줍니다.

print(days)
# 날의 수를 출력해줍니다.