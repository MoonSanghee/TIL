while True:
    numbers = list(map(int, input().split()))
    if len(numbers) == 1 and numbers[0] == -1:
        break
    # 수열이 -1이 나올때까지 받아줍니다.
    result = 0
    for i in range(len(numbers) - 1):
        if numbers[i] % 2 == 0:
            if numbers[i] // 2 in numbers:
                result += 1
    # 모든 수를 확인하며 각 수를 2로 나눈 값이 수열에 몇개나 있는지 확인해줍니다.
    print(result)
    # 찾은 수의 개수를 출력해줍니다.