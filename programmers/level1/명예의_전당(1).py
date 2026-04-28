from collections import deque

def solution():
    answer = []
    members = deque()
    # 명예의 전당을 담을 덱을 만들어줍니다 
    for i in score:
        for j in range(len(members)):
            if members[j] >= i:
                members.insert(j, i)
                break
        else:
            members.append(i)
        # 주어지는 점수를 확인하여 명예의 전당에 득표대로 넣어줍니다
        if len(members) > k:
            members.popleft()
        # 인원이 제한을 초과하면 최저점자를 방출합니다
        answer.append(members[0])
        # 남은 멤버중에 최저득점자를 정답에 추가해줍니다
    return answer
    # 결과를 출력해줍니다