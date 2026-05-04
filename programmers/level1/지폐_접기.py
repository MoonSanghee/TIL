def solution(wallet, bill):
    answer = 0
    wallet = [min(wallet), max(wallet)]
    # 지갑의 긴 면과 짧은 면을 구별해줍니다
    while True:
        if bill[0] > bill[1]:
            bill[0],bill[1] = bill[1], bill[0]
        # 지폐의 긴면과 짧은면을 지갑과 동일하게 맞춰줍니다
        if bill[0] <= wallet[0] and bill[1] <= wallet[1]:
            break
        else:
            bill[1] //= 2
            answer += 1
        # 지갑에 들어가는지 확인하고 들어가지않으면 한 번 더 접어줍니다
    return answer
    # 결과를 출력해줍니다