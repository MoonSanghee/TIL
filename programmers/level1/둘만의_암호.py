def solution(s, skip, index):
    answer = ''
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    # a부터 z까지 알파벳을 나열해줍니다.
    for c in skip:
        if c in alpha:
            alpha = alpha.replace(c, "")
        # 스킵에 포함된 문자라면 replace메서드를 이용하여 없애줍니다.
    
    for i in s:
        change = alpha[(alpha.index(i) + index) % len(alpha)]
        answer += change
        # 새로운 기준의 alpha에서 바꿀 문자를 찾아 answer에 넣어줍니다.
    return answer