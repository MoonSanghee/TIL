t = int(input())
# 테스트 케이스가 몇개인지 받아줍니다.
for tc in range(t):
    n = int(input())
    # 게임에 참여하는 사람수를 받아줍니다.
    d = dict()
    for i in range(n):
        d[i + 1] = int(input())
    # 각 플레이어가 지명한 사람을 키, 밸류로 딕셔너리에 담아줍니다.
    passed = set()
    cnt = 0
    player = 1
    # 지명당한 사람들을 담을 리스트를 만들고 게임이 진행된 턴, 현재 지명하는 사람을 변수에 담아줍니다.
    while True:
        passed.add(player)
        cnt += 1
        player = d[player]
        # 지명하는 사람을 리스트에 담고 지명한 사람으로 이동해줍니다.
        if player in passed:
            print(0)
            break
        # 이미 지명된적 있는 사람이라면 주경이에게 도달하지 못하므로 0을 출력해줍니다.
        elif player == n:
            print(cnt)
            break
        # 지명당한것이 주경이라면 몇 도달한 수를 출력해줍니다.
        