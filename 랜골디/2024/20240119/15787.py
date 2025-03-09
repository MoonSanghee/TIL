n, m = map(int, input().split())
trains = [[False] * 20 for _ in range(n)]
# 열차의 수와 명령을 받고 n개의 열차를 만들어 줍니다.
for _ in range(m):
    command = list(map(int, input().split()))
    if command[0] == 1:
        trains[command[1] - 1][command[2] - 1] = True
    elif command[0] == 2:
        trains[command[1] - 1][command[2] - 1] = False
    elif command[0] == 3:
        for i in range(19, 0, -1):
            trains[command[1] - 1][i] = trains[command[1] - 1][i - 1]
        trains[command[1] - 1][0] = False
    else:
        for i in range(19):
            trains[command[1] - 1][i] = trains[command[1] - 1][i + 1]
        trains[command[1] - 1][19] = False
    # 명령어를 실행시켜줍니다.
result = []
for train in trains:
    if train not in result:
        result.append(train)
# 빈 리스트에 같은 상태의 기차가 없는지 확인하여 처음 나온 상태의 기차만 추가해줍니다.
print(len(result))
# 다른 상태의 기차 수를 출력해줍니다.