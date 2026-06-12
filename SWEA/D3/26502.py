T = int(input())
# 테스트케이스의 개수를 받아줍니다
for t in range(T):
    n = int(input())
    dots = []
    for _ in range(n):
        dots.append(list(map(int, input().split())))
    # 주어지는 좌표의 개수를 받고 좌표들을 리스트에 담아줍니다
    result = 0
    # 결과를 담을 변수를 설정해줍니다
    for i in range(n):
        length = [0, 0]
        # 각 점에서 빗변이 아닌 변들의 길이를 담을 변수를 설정해줍니다
        for j in range(n):
            if i != j:
                if dots[i][0] == dots[j][0]:
                    length[1] = max(length[1], abs(dots[i][1] - dots[j][1]))
                elif dots[i][1] == dots[j][1]:
                    length[0] = max(length[0], abs(dots[i][0] - dots[j][0]))
        result = max(result, length[0] * length[1])
        # 넓이가 최대가 되는 구간을 확인하여 결과와 비교해줍니다
    print(result)
    # 결과를 출력해줍니다