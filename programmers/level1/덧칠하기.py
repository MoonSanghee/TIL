def solution(n, m, section):
    answer = 0
    if section:
        # 패인트 칠할 부분이 존재한다면
        s = section[0]
        e = s + m - 1
        answer += 1
        # 패인트 칠을 시작하는 부분을 가장 먼저 오는 칠 할 부분으로 설정하고 마지막 부분을
        # 시작 부분에서 한 번에 칠해지는 길이까지로 정해주고 1번 칠했음을 표시해줍니다.
        for i in section:
            if e < i:
                s = i
                e = s + m - 1
                answer += 1
                # 칠 할 부분이 이전에 칠 했던 부분을 벗어나면 새로 칠할때 
                # 덮을수 있는 부분을 갱신해주고 1번 더 칠했으니 answer값을 1 더해줍니다.
    return answer
    # answer에 저장된 값을 리턴해줍니다.