def solution(age):
    answer = ''
    letters = 'abcdefghij'
    for i in str(age):
        answer += letters[int(i)]
    return answer