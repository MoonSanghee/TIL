def solution(n, words):
    answer = [0, 0]
    # 정답을 통과되는 [0,0]으로 설정해줍니다.
    used = set()
    used.add(words[0])
    # 사용한 단어들을 담아줄 세트형 자료구조를 만들고 첫번째 단어를 넣어줍니다.
    letter = words[0][-1]
    # 첫번째 단어의 마지막 문자를 담아줍니다.
    for i in range(1, len(words)):
        if words[i][0] != letter or words[i] in used:
        # 단어들을 순회하며 단어의 시작 문자와 저장되어있는 이전 단어의 마지막
        # 문자를 비교하여주고 단어가 사용된 적 있는지 확인해줍니다.
            answer[0] = i%n + 1
            answer[1] = i // n + 1
            break
        # 말이 이어지지 않거나 사용된 적 있다면 answer[0]을 i%n + 1을 계산해 몇 번째 
        # 사람인지 찾아주고 answer[1]은 i // n + 1로 몇번을 순회했는지 저장해주고 반복을 멈춥니다.
        else:
            letter = words[i][-1]
            used.add(words[i])
            # 단어도 이어지고 처음 나온 단어라면
            # 문자를 새로 부른 단어의 마지막 문자로 바꾸어주고 사용한 단어에 넣어줍니다.
    return answer
    # answer에 저장된 값을 돌려줍니다.