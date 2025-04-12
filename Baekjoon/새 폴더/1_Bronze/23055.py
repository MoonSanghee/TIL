n = int(input())
# 표지판의 크기를 받아해줍니다
for i in range(n):
    line = ''
    for j in range(n):
        if i in (0, n - 1) or j in (0, n - 1):
            line += '*'
        # 가로나 세로의 위치가 0이나 n - 1이라면 테두리이므로 모두 *표시가 와야합니다
        elif j == i or n - 1 - j == i:
            line += '*'
        # i와 j값이 같거나 n - 1에 i를 뺀 값이 j와 같다면 X표시가 위치하는 자리이므로 *표시가 와야합니다
        else:
            line += ' '
        # 그 외의 자리는 공백이므로 빈 공간을 넣어줍니다
    print(line)
    # 각 줄별로 완성하여 차례대로 출력해줍니다