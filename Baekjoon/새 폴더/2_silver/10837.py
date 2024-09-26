k = int(input())
c = int(input())
# 라운드와 테스트 케이스의 수를 받아줍니다.
for _ in range(c):
    n, m = map(int, input().split())
    # 두 사람의 점수를 바아줍니다.
    flag = False
    if n == m:
        flag = True
    elif n > m:
        if k - n + 1 >= n - 1 - m:
            flag = True
    elif n < m:
        if k - m >= m - 1 - n:
            flag = True
    # 점수가 나올수있는지 확인해줍니다.
    if flag:
        print(1)
    else:
        print(0)
        # 결과를 출력해줍니다.