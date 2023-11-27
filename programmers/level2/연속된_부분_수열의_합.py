def solution(sequence, k):
    n = len(sequence)
    # 수열의 길이를 확인해줍니다.
    answer = [0, n]
    # 가장 앞 인덱스와 가장 뒤 인덱스를 answer에 넣어줍니다.
    s, e = 0, 0
    result = sequence[0]
    # 수열의 시작과 끝을 가장 앞 인덱스로 설정하고 수열의 합을 담을 변수에 맨 앞의 인덱스 값을 담아줍니다.
    while True:
        if result < k:
            e += 1
            if e == n:
                break
            result += sequence[e]
            # 수열의 합이 k보다 작으면 수열이 더 늘어날수 있는지 확인하고 
            # 늘어날 수 있다면 값을 더하고 없다면 확인을 멈추어줍니다.
        else:
            if result == k:
                if e - s < answer[1] - answer[0]:
                    answer = [s, e]
            result -= sequence[s]
            s += 1
            # 수열의 합이 k이면 길이를 현재 answer에 담긴 수열의 길이와 비교하여 짧은것을 넣어줍니다.
            # 수열의 합에서 가장 앞 값을 빼고 시작을 오른쪽으로 한 칸 보내줍니다.
    return answer
    # answer에 담긴 수열을 return해줍니다.