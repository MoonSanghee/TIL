n, m = map(int, input().split())
lamps = list(map(int, input().split()))
# 전구의 개수와 명령어의 수 램프의 초기 상태를 받아줍니다
for _ in range(m):
    a, b, c = map(int, input().split())
    # 명령어를 받아줍니다
    if a == 1:
        lamps[b - 1] = c
    elif a == 2:
        for i in range(b - 1, c):
            if lamps[i] == 1:
                lamps[i] = 0
            else:
                lamps[i] = 1
    elif a == 3:
        for i in range(b - 1, c):
            lamps[i] = 0
    elif a == 4:
        for i in range(b - 1, c):
            lamps[i] = 1
    # 명령어에 따른 실행을 진행할여줍니다
print(*lamps)
# 결과를 주어진 형식대로 출력하여줍니다