tc = int(input())
# 연산을 입력받을 횟수를 받아줍니다.
for _ in range(tc):
    mars = list(map(str, input().split()))
    #  시행할 연산을 받아줍니다.
    answer = 0
    for i in range(len(mars)):
        if i == 0:
            answer += float(mars[i])
        else:
            if mars[i] == "#":
                answer -= 7
            elif mars[i] == "%":
                answer += 5
            elif mars[i] == "@":
                answer *= 3
    # 수식만큼 연산을 실행해줍니다.
    print("%0.2f" % answer)
    # 소수점 2번째자리까지 출력해줍니다.