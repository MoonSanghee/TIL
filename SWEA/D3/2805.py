test = int(input())
for t in range(1, test + 1):
    n = int(input())
    seet = []
    for i in range(n):
        line = list(map(int, input()))
        seet.append(line)

    result = 0
    s, e = n // 2, n // 2
    for i in range(n):
        for j in range(s, e + 1):
            result += seet[i][j]
        if i < n // 2:
            s -= 1
            e += 1
        else:
            e -= 1
            s += 1
    print(f'#{t} {result}')

# 찾아본 코드
# T = int(input())
# for test_case in range(1, T + 1):
#     N = int(input())
#     farm = [list(map(int, list(input().strip()))) for _ in range(N)]

#     m = N // 2  # 중심
#     answer = 0
#     for i in range(m+1):  # 위아래가 대칭이므로 절반까지만 구한다.
#         for j in range(m - i, m + i + 1):  # 중심을 기준으로 왼쪽으로 1칸, 오른쪽으로 1칸 범위를 늘려 나간다.
#             answer += farm[i][j] + farm[N-i-1][j]

#     print(f'#{test_case} {answer - sum(farm[m])}')  # 가운데를 두번 더해줬으므로 한번은 다시 빼준다.