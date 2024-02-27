t = int(input())
# 테스트 케이스의 수를 받아줍니다.
for _ in range(t):
    input()
    # 빈 값을 받기때문에 입력을 담지 않습니다.
    n, m = map(int, input().split())
    c = list(map(int, input().split()))
    b = list(map(int, input().split()))
    # n과 m의 값을 받고 c언어와 경제학 학생의 iq를 받아줍니다.
    ca = sum(c) / n
    ba = sum(b) / m
    # 두 과목의 평균 iq를 받아줍니다.
    cnt = 0
    for i in c:
        if ca > i and ba < i:
            cnt += 1
        # c과목을 드랍하고 경제학 수업을 듣는데 두 과목 학생 평균 iq를 다 올려야하므로
        # c언어 평균 아래 경제학 평균보다 높은 학생의 수를 확인해줍니다.

    print(cnt)
    # cnt에 담긴 값을 출력해줍니다.