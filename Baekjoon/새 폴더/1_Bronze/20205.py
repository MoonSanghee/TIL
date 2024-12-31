n, k = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
# n과 k를 받고 최초 그림을 받아줍니다

for i in range(n):
    for _ in range(k):
        for j in range(n):
            for _ in range(k):
                print(maps[i][j], end = ' ')
                # 각 줄에 k배씩 출력되야하므로 줄이 바꾸지 않고 띄워주기만 합니다
        print()
        # 각 줄이 끝나면 줄을 바꿔줍니다