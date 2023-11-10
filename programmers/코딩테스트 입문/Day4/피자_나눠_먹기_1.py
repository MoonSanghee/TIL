def solution(n):
    answer = 0
    while True:
        answer += 1
        if (answer * 7)//n >= 1:
            break
    return answer