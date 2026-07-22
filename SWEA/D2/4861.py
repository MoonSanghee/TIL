T = int(input())
# 테스트케이스의 개수를 받아줍니다
for t in range(T):
    n, m = map(int, input().split())
    # 주어지는 표의 크기와 찾을 회문의 길이를 받아줍니다
    base = [list(input()) for _ in range(n)]
    cross = [list(row) for row in zip(*base)]
    reuslt = ''
    # 주어진 표를 받고 행,열을 뒤집은 표도 만들어줍니다
    for i in range(n):
        for j in range(n - m + 1):
            row = base[i][j:j + m]
            column = cross[i][j:j + m]
            if row == row[::-1]:
                result = row
            if column == column[::-1]:
                result = column
    # 각 행열을 순회하며 주어진 길이의 회문을 찾아줍니다
    result = ''.join(result)
    print(f'#{t + 1} {result}')
    # 결과를 주어진 양식에 맞춰 출력해줍니다