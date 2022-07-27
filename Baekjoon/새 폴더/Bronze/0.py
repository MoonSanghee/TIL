def solution(numbers):
    result = []
    for overlap in numbers:
        if numbers.count(overlap) >=2:
            result.append(2 * overlap)

    for i in range(len(numbers)):
        a = sorted(list(set(numbers)))
        b = list(reversed(a))
        if i >= len(b):
            break
        for j in b[:len(a) - i - 1:]:
            result.append(a[i] + j)
    result = sorted(list(set(result)))
    
    return result
print(solution([2,1,3,4,1]))

