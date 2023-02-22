def solution(s):
    answer = []
    d = dict()
    for i in range(len(s)):
        if s[i] in d:
            answer.append(i - d[s[i]])
            d[s[i]] = i
        else:
            d[s[i]] = i
            answer.append(-1)
        # 단어를 순회하며 문자가 나온적 없다면 answer에 -1을 넣어주고 
        # d의 s[i]에 i를 넣어주고 나온적 있다면 i - d[s[i]]을 answer에 넣어주고
        # d의 s[i] 값을 갱신해줍니다.
    return answer