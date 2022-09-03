import sys
sys.stdin = open('test.txt', 'r')
n = int(input())
mat = []
check = []
mx = 2
mn = 100
for i in range(n):
    line = list(map(int, input().split()))
    mat.append(line)
    mx = max(max(line), mx)
    mn = min(min(line), mn)

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

def dfs(i, j, high):
    stack = list()
    stack.append((i, j))
    check[i][j] = 1

    while stack:
        x, y = stack.pop()
        for d in range(4):
            ni = x + di[d]
            nj = y + dj[d]
            if ni in range(n) and nj in range(n):
                if mat[ni][nj] >= high and check[ni][nj] == 0:
                    check[ni][nj] = 1
                    stack.append((ni, nj))
result = 0
for high in range(mn, mx + 1):
    check = []
    for i in range(n):
        l = []
        for j in range(n):
            l.append(0)
        check.append(l)
    cnt = 0
    for i in range(n):
        for j in range(n):
            if mat[i][j] >= high and check[i][j] == 0:
                cnt += 1
                dfs(i, j, high)
    result = max(result, cnt)
print(result)

# 비의 양에 따른 모든 경우를 다 조사해 보면 물에 잠기지 않는 안전한 영역의 개수 중에서 최대인 경우는 5임을 알 수 있다. 
# 문제를 자세히 읽어보면 비가 내릴 양은 정해지지 않고 모든 경우를 다 가정했을경우 가장 많은 수의 덩어리를 가지는 갯수가 몇 개인지
# 찾으면 됨을 알 수 있다.