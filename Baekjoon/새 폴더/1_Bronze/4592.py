while True:
    numbers = list(map(int, input().split()))
    # 주어지는 수열을 받아줍니다
    if numbers[0] == 0:
        break
    # 마지막 입력인지 확인해줍니다
    print(numbers[1], end=' ')
    for i in range(1, numbers[0]):
        if numbers[i + 1] != numbers[i]:
            print(numbers[i + 1], end=' ')
    # 이전수와 같은지 확인하여 다르다면 출력하여줍니다
    print('$')
    # 수의 입력이 끝났으니 $을 출력해줍니다