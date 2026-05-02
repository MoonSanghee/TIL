def solution(k, m, score):
    answer = 0
    score.sort()
    # 주어진 사과의 정보를 오름차순으로 정렬해줍니다
    while score:
        minimum = score[-1]
        # 최고점의 사과 등급을 변수에 담아줍니다
        for _ in range(m):
            if len(score) == 0:
                break
        # 상자를 완성할만큼 사과가 충분하지않다면 반복을 멈추어줍니다
            minimum = score.pop()
        # 사과가 부족하지않다면 사과의 최저점을 갱신해줍니다
        else:
            answer += minimum * m  
        # 상자가 완성되었다면 점수를 계산하여 결과에 더해줍니다
    return answer
    # 주어진 사과를 전부 사용하였다면 최종 점수를 출력해줍니다