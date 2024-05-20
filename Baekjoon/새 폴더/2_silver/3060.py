t = int(input())
# 테스트 케이스가 몇개인지 받아줍니다.
for _ in range(t):
    n = int(input())
    food = sum(list(map(int, input().split())))
    # 배달받는 사료의 양과 필요한 사료의 양을 받아줍니다.
    day = 1
    # 몇일까지 돼지를 먹일수있는지 담을 변수를 설정해줍니다.
    while True:
        if n < food:
            break
        # 배달받는 사료가 부족하다면 계산을 멈추어줍니다.
        day += 1
        food *= 4
        # 다음날 필요한 사료의 양은 각 돼지마다 양 옆과 마주보는 돼지의 사료 양이 추가되므로 합이 4배 증가합니다.
    print(day)
    # 몇일까지 돼지들의 요구대로 먹이를 줄 수 있는지 출력해줍니다.