while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    # n, m을 받아줍니다.

    ranks = dict()
    # 플레이어들의 랭킹 포인트를 담을 딕셔너리를 만들어줍니다.
    for _ in range(n):
        scores = list(map(int, input().split()))
        for i in range(m):
            if scores[i] in ranks:
                ranks[scores[i]] += 1
            else:
                ranks[scores[i]] = 1
    # 랭킹에 오른 플레이어들의 랭킹 포인트를 추가하여줍니다.
    
    first = [0, []]
    second = [0, []]

    for p in ranks:
        if ranks[p] > first[0]:
            second[0], second[1] = first[0], first[1]
            first[0] = ranks[p]
            first[1] = [p]
        # 최고점이 갱신되었다면 기존의 최고점과 최고점 유저들을 차고점으로 이동하고 최고점 기록과 플레이어를 갱신하여줍니다.
        elif ranks[p] == first[0]:
            first[1].append(p)
        # 최고점 유저와 동점이라면 최고점 유저에 추가하여줍니다.
        elif ranks[p] > second[0]:
            second[0] = ranks[p]
            second[1] = [p]
        # 최고점 이하 차고점 이상이라면 차고점의 점수와 유저를 갱신하여줍니다.
        elif ranks[p] == second[0]:
            second[1].append(p)
        # 차고점과 동률이라면 차고점 유저 목록에 추가하여줍니다.
    
    players = sorted(second[1])
    print(*players)
    # 차고점 유저 목록을 오름차순으로 정렬하여 출력해줍니다.