def solution(numer1, denom1, numer2, denom2):
    son, mom = numer1 * denom2 + numer2 * denom1, denom1 * denom2
    for i in range(mom, 1, -1):
        if son % i == 0 and mom % i == 0:
            son //= i
            mom //= i
            break
    return [son, mom]