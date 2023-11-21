def solution(users, emoticons):
    answer = [0, 0]
    discount_combinations = []
    dfs(len(emoticons), [], discount_combinations)
    # 적용할 수 있는 모든 할인 조합을 찾아줍니다.
    for discount in discount_combinations:
        # 할인 조합을 순회하며
        cnt = 0
        income = 0
        # 구독을 할 유저의 수와 수입을 저장할 변수를 설정해줍니다.
        for want, limit in users:
            # 유저를 순회하며
            budget = 0
            for i in range(len(discount)):
                if discount[i] >= want:
                    budget += emoticons[i] * (100 - discount[i]) / 100
            # 할인율이 유저의 희망하는 수준 이상이라면 결제하도록 합니다.
            if budget >= limit:
                cnt += 1
                # 유저의 총 결제액이 구독을 할 수준이라면 cnt에 값을 1 더하고
            else:
                income += budget
                # 아니라면 이모티콘을 구입하니 income에 budget을 더해줍니다.
        if cnt >= answer[0]:
            # 모든 유저를 확인하고 
            if cnt == answer[0]:
                answer[1] = max(answer[1], income)
            # 구독할 유저가 같다면 이모티콘 판매수익을 비교하여 높은 값으로 갱신하고
            else:
                answer[1] = income
                answer[0] = cnt
             # 더 많다면 수입과 구독자 수를 갱신해줍니다.
    return answer
    # 구독자와 수입이 담긴 리스틑 answer를 리턴해줍니다.

def dfs(target, com, discount_combinations):
    # 할인 조합을 만드는 함수입니다.
    if len(com) == target:
        discount_combinations.append(com.copy())
    # com리스트에 조합이 완성되었다면 discount_combinations에 추가해줍니다.
    else:
        for i in [10, 20, 30, 40]:
            com.append(i)
            dfs(target, com, discount_combinations)
            com.pop()
        # 아니라면 받은 com에 할인율을 추가하여 discount_combinations에 추가하여 
        # 함수를 다시 실행시켜줍니다.