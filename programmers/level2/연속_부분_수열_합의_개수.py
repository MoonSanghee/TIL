def solution(elements):
    numbers = set()
    # 연속한 부분의 합을 담을 세트형 자료를 설정해줍니다
    n = len(elements)
    # 주어지는 수열의 길이를 구해줍니다
    for i in range(n):
        number = elements[i]
        numbers.add(number)
        # 주어진 수열을 순회하며 각 수로 시작하는 수열을 확인해줍니다
        for j in range(i + 1, n + i):
            number += elements[j % n]
            numbers.add(number)
        # 수열의 각 수에서 시작하는 연속한 수열의 합을 구해 세트에 넣어줍니다
    return len(numbers)
    # 합의 개수를 출력해줍니다