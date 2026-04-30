def solution(k, tangerine):
    answer = 0
    # 결과를 담을 변수를 설정해줍니다
    d = dict()
    # 각 귤의 크기별 개수를 담을 딕셔너리를 설정해줍니다
    for i in tangerine:
        d[i] = d.get(i, 0) + 1
    # 각 귤의 크기별 개수를 딕셔너리에 담아줍니다
    d = dict(sorted(d.items(), key = lambda x : x[1], reverse = True))
    # 딕셔너리를 크기별 개수를 기준으로 내림차순 정렬을 해줍니다
    for i in d:
        if k <= 0:
            break
        # 필요한 개수를 충족했는지 확인하여줍니다
        k -= d[i]
        answer += 1
        # 귤의 개수를 빼주고 종류를 1 더해줍니다
    return answer
    # 결과를 돌려줍니다