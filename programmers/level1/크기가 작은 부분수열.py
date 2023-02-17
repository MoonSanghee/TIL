def solution(t, p):
    answer = 0
    length = len(p)
    for i in range(len(t) - length + 1):
        if int(t[i:i+length]) <= int(p):
            answer += 1
    return answer
    # 문자열 t안에 p길이와 같은 이어지는 문자열을 정수형으로 변환하여 p의 정수형
    # 값과 비교한 후 작거나 같다면 answer에 누적하여 세어주었습니다.