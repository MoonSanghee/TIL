while True:
    n = input()
    if n == '0':
        break
    # 0이 입력될때까지 진행합니다.
    numbers = [n]
    # 입력받은 수를 리스트에 담아줍니다.
    while True:
        if len(numbers[-1]) == 1:
            break
        # 마지막에 위치한 수가 한자리수일때까지 실행합니다
        last = numbers[-1]
        number = 1

        for i in last:
            number *= int(i)
        # 마지막 수의 각 자리 값을 곱해 나오는 수를 구해줍니다.
        numbers.append(str(number))
        # 각자리 수를 모두 곱한 값을 리스트에 넣어줍니다.
    
    print(*numbers)
    # 한자리수가 되는 과정을 출력해줍니다.