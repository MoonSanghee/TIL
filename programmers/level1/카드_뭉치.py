def solution(cards1, cards2, goal):
    answer = 'Yes'
    # answer에 기본값을 'Yes'로 설정해줍니다.
    first = 0
    second = 0
    # 첫번째 카드 뭉치의 확인할 위치를 담을 first와 두번째 카드 뭉치의 위치를
    # 담을 second를 설정해줍니다.
    for i in range(len(goal)):
        if len(cards1) > first and cards1[first] == goal[i]:
            first += 1
            # cards1의 크기가 first보다 크고 cards1에서 확인할 위치가 goal에
            # 오는 값과 같다면 first의 값을 1 더해줍니다.
        elif len(cards2) > second and cards2[second] == goal[i]:
            second += 1
            # cards2의 크기가 second보다 크고 cards2에서 확인할 위치가 goal에 
            # 오는 값과 같다면 second의 값을 1 더해줍니다.
        else:
            answer = 'No'
            break
        # card1과 card2에서 goal에 와야하는 단어가 올 수 없다면 answer를 'No'로
        # 바꾸고 출력해줍니다. 
    return answer