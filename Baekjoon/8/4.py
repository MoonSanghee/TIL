# 8-4 문제번호 1929

m, n = map(int, input().split())
for i in range(m, n + 1):
    check_list = []
    for j in range(2, i):
        if i % j == 0:
            check_list.append(j)
    if len(check_list) == 2:
        print(check_list[1])

