def queen(x):
    # 퀸이 그 자리에 놓일수 있는지 확인하는 함수입니다.
    for i in range(x):
        if chess[x] == chess[i] or abs(chess[x] - chess[i]) == abs(x - i):
        # 같은 열이나 대각선 위치를 확인하여 퀸이 이미 놓여있는지를 확인해줍니다.
            return False
    return True

def visit(x):
    # 퀸을 새로 놓는 함수입니다.
    global cnt
    if x == n:
        cnt += 1
        # 모든 퀸을 둘 수 있었다면 경우의 수가 1가지 더 발견된 것이므로 cnt 값을 1증가시켜줍니다.
    else:
        for i in range(n):
            chess[x] = i
            # 행의 모든 열을 순회하며 퀸을 놓고
            if queen(x):
                visit(x + 1)
                # 놓일수 있는지 확인하고 퀸이 놓일수 있는 위치라면 다음 행으로 넘어가 시행해줍니다.

n = int(input())
cnt = 0
chess = [0] * n

visit(0)
print(cnt)