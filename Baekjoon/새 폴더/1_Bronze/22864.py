work, get, rest, limit = map(int, input().split())
# 일을 할 때 받는 피로도, 작업량, 휴식으로 회복되는 피로도, 최대 피로도를 받아줍니다.
health = 0
result = 0
# 현재 피로도와 작업량을 담을 변수를 설정해줍니다.
for _ in range(24):
    if health + work > limit:
        health -= rest
        if health < 0:
            health = 0
    # 일을 했을때 피로도가 한계를 넘어선다면 휴식을 취해줍니다.
    else:
        health += work
        result += get
    # 일을 할 수 있다면 일을 진행하고 결과를 적용시킵니다.

print(result)
# 작업을 얼마나 진행하였는지 출력해줍니다.