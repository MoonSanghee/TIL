from itertools import permutations

def solution(babbling):
    answer = 0
    base = ["aya","ye","woo","ma"]
    check = []
    for i in range(1, 5):
        for word in permutations(base, i):
            check.append(''.join(word))
            
    for i in babbling:
        if i in check:
            answer += 1
    return answer