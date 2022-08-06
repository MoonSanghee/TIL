test_case = int(input())
for test in range(1, test_case + 1):
    n = int(input())
    seet = [[0 for _ in range(n)] for _ in range(n)]
    # n * n의 크기에 각 인덱스 값을 0으로 가지는 시트를 만들어 준다.
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    # 횡, 열을 이동 시킬 경우 우, 하, 좌, 상을 각 인덱스에 저장하여 준다.
    num = 1
    curve = 0
    i, j = 0, 0
    # 첫자리에 올 숫자와 꺾은 횟수와 각 자리 값을 저장해줄 값을 설정해준다.
    while num < n**2 + 1:
        # n * n 크기의 시트이기때문에 가장 큰 값은 n의 제곱이기 때문에 n의 제곱이 들어갈 떄까지 반복해준다.
        seet[i][j] = num
        num += 1
        # 시트의 자릿값에 숫자를 대입해주고 1씩 증가시켜준다.
        check_i = i + di[curve]
        check_j = j + dj[curve]
        # 그 다음 움직임이 이전 시행과 동일해도 되는지 확인할 값을 설정해준다.
        if check_i < 0 or check_i >= n or check_j < 0 or check_j >= n or seet[check_i][check_j] !=0:
        # if check_i not in range(n) or check_j not in range(n) or seet[check_i][check_j] !=0: 
        # 아래와 같이 표현도 가능
            curve += 1
            curve = curve % 4
        # 설정해준 값이 시트의 크기를 벗어났거나 움직였을때 덮었을 값이 0이 아니면 꺾어줘야 하기 때문에 
        # 1번의 움직임을 추가해주는데 이 때 우, 하, 좌, 상의 방향을 주기로 돌기에 더한 값에 4로 나눈 나머지를 새로 저장해준다.
        i += di[curve]
        j += dj[curve]
        # 확인후 현재 이동 방향에 따라 i와 j의 값을 변경해준다.
    print(f'#{test}')
    for i in range(n):
        for j in range(n):
            print(seet[i][j], end = ' ')
        print()