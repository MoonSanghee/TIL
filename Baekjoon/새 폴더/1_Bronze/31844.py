maps = input()
# 주어지는 배치를 받아줍니다
for i in range(10):
    if maps[i] == '@':
        robot = i
    elif maps[i] == '!':
        target = i
    elif maps[i] == '#':
        box = i
# 로봇과 박스, 목표지점의 위치를 찾아줍니다
if robot < box < target or robot > box > target:
    print(abs(robot - target) - 1)
    # 로봇이 박스를 밀어 타겟에 도착할 수 있다면 몇 칸을 움직여야하는지 출력해줍니다
else:
    print(-1)
    # 타겟에 도착할 수 없다면 -1을 출력해줍니다