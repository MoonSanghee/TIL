def solution(my_string, n):
    answer = ''
    my_string = list(my_string)
    for letter in my_string:
        answer += letter * n
    return answer