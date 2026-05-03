def solution(babbling):
    answer = 0
    words =  ["aya", "ye", "woo", "ma"]
    # 발음할수있는 단어를 리스트에 담아줍니다
    for b in babbling:
        # 주어진 단어를 순회하며 확인해줍니다
        for i in words:
            if i * 2 not in b:
                # 발음할수있는 단어가 연속헤서 나오지 않는지 확인해줍니다
                b = b.replace(i, ' ')
                # 발음할수있는 옹알이를 제거해줍니다
        if b.isspace():
            answer += 1
        # 발음하지못하는 단어가 없다면 결과를 갱신해줍니다
        
    return answer
    # 결과를 출력해줍니다