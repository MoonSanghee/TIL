while True:
    numbers = list(map(int, input().split()))
    # 세 수를 받아줍니다.
    if numbers[0] == numbers[1] == numbers[2] == 0:
        break
    # 세 수가 모두 0이면 확인을 멈추어줍니다.
    if numbers[2] - numbers[1] == numbers[1] - numbers[0]:
        next = numbers[2] + numbers[1] - numbers[0]
        print(f'AP {next}')
    # 앞의 두 수의 차와 뒤 두 수의 차가 같다면 등차수열이므로 마지막 수에 차를 더한값을 출력해주고
    else:
        next = numbers[2] * numbers[1] // numbers[0]
        print(f'GP {next}')
    # 아니라면 등비수열이므로 마지막 수에 증가하는 만큼 곱한 값을 출력해줍니다.