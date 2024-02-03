def solution(name, yearning, photo):
    answer = []
    d = dict()
    for i in range(len(name)):
        if i in range(len(yearning)):
            d[name[i]] = yearning[i]
    # 그리운 사람의 점수를 매칭시켜줍니다.
    for line in photo:
        result = 0
        for i in line:
            if i in d:
                result += d[i]
            # 그리운 사람이라면 점수를 더해줍니다.
        answer.append(result)
        # 더한 결과를 answer에 넣어줍니다.
    return answer