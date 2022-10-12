tc = int(input())
for test in range(tc):
    cvs = int(input())
    home = list(map(int, input().split()))
    maps = [home]
    for i in range(cvs + 1):
        maps.append(list(map(int, input().split())))
    for i in range(cvs + 1):
        length = abs(maps[i][0] - maps[i + 1][0]) + abs(maps[i][1] - maps[i + 1][1])
        if length > 1000:
            print('sad')
            break
    else:
        print('happy')