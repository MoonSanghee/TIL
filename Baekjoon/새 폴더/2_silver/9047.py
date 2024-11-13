n = int(input())
# 주어지는 수의 개수를 받아줍니다
for _ in range(n):
    number = int(input())
    cnt = 0
    # 주어지는 수를 받고 실행한 연산 횟수를 담을 변수를 설정해줍니다
    while True:
        if number == 6174:
            break
        # 목표에 도달하였다면 연산을 멈추어줍니다
        cnt += 1
        line = list(str(number))
        number = int(''.join(sorted(line, reverse=True))) - int(''.join(sorted(line)))
        # 연산 횟수를 증가시키고 연산을 실행시켜줍니다
        while number < 1000:
            number *= 10
        # 연산 결과가 1000이하라면 10씩 곱해주며 4자리수로 맞추어줍니다
    print(cnt)
    # 연산 횟수를 출력해줍니다