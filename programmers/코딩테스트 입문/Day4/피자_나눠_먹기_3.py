def solution(slice, n):
    answer = 0
    while True:
        if (answer * slice)//n > 0:
            break
        answer += 1
    return answer