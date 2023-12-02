def solution(n):
    answer = ''
    while n:
        # n이 0이 될때까지 시행하여줍니다.
        answer += str(n % 3)
        # answer에 n을 3으로 나눈 나머지를 문자열형태로 받아줍니다.
        n //= 3
        # n을 3으로 나눈 몫으로 갱신해줍니다.
    return int(answer, 3)
    # int함수를 이용하여 3진법 answer를 10진법으로 전환하여줍니다