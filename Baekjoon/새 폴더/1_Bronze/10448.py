tri = [i * (i + 1) // 2 for i in range(1, 46)]
# 주어지는 수가 1000보다 작으므로 1000 이하 크기의 모든 삼각형의 크기를 구해줍니다.
check = [0] * 1001
# 1000까지 조합할 수 있는지 체크할 리스트를 만들어줍니다.
for i in tri:
    for j in tri:
        for k in tri:
            num = i + j + k
            if num <= 1000:
                check[num] = 1
# 삼각형 세 개를 조합하여 나오는 값은 만들수 있다고 표시해줍니다.
t = int(input())
# 입력받을 수가 몇개인지 받아줍니다.
for _ in range(t):
    n = int(input())
    print(check[n])
    # 조합으로 나올수 있는 값인지 확인하고 결과를 출력해줍니다.