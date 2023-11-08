def solution(array):
    dict = {}
    for i in array:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    num = -1
    cnt = 0
    for k in dict:
        if dict[k] > cnt:
            num = k
            cnt = dict[k]
        elif dict[k] == cnt:
            num = -1
    return num