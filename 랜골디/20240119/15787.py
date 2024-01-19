n, m = map(int, input().split())
trains = [[False] * 20 for _ in range(n)]
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

result = []
for train in trains:
    if train not in result:
        result.append(train)

print(len(result))