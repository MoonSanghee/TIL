def solution(n):
    answer = 1
    while True:
        if answer * 6 % n == 0:
            break
        else:
            answer += 1
    return answer