T = int(input())
# 테스트케이스의 개수를 받아줍니다
for t in range(T):
    n = int(input())
    maps = [[0]* 11 for _ in range(11)]
    result = 0
    # 주어지는 영역의 개수와 칠할 영역, 결과를 담을 변수를 설정해줍니다
    for _ in range(n):
        info = list(map(int, input().split()))
        for i in range(info[0], info[2] + 1):
            for j in range(info[1], info[3] + 1):
                if maps[i][j] != 0:
                    if maps[i][j] != info[-1]:
                        maps[i][j] = 3
                else:
                    maps[i][j] = info[-1]
    # 영역의 정보를 순회하며 영역을 칠해줍니다
    for i in range(11):
        for j in range(11):
            if maps[i][j] == 3:
                result += 1
    # 겹쳐 칠해진 영역의 개수를 확인해줍니다
    print(f'#{t + 1} {result}')
    # 결과를 출력해줍니다