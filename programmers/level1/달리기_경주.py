def solution(players, callings):
    rank = {player: i for i, player in enumerate(players)}
    # 플레이어의 순서대로 순위를 매칭시켜 딕셔너리에 담아줍니다.
    for name in callings:
        idx = rank[name]
        # 현재 순위를 담아줍니다.
        rank[name] -= 1
        rank[players[idx - 1]] += 1
        # 이름이 불린 선수의 순위를 하나 줄여주고 앞에 있던 선수를 찾아 밀려난것을 표시해줍니다.
        players[idx], players[idx - 1] = players[idx - 1], players[idx]
        # players 리스트에서 역전한 선수와 당한 선수의 위치를 바꾸어줍니다.
    return players
# players의 순위가 담긴 리스트를 return합니다.