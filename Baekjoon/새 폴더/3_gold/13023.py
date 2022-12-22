n, m = map(int, input().split())

li = [[] for _ in range(n)]
# 관계를 표시해줄 관계리스트입니다
check = [False for _ in range(2001)]
# 방문을 확인하는 리스트입니다.
result = False
# 깊이가 충분한지는 기본을 False로 설정합니다.

for i in range(m):
    a, b = map(int, input().split())
    li[a].append(b)
    li[b].append(a)
    # 입력되는 관계에 따라 양방향 그래프를 표시해줍니다.

def dfs(x, y):
    global result
    check[x] = True
    if y == 4:
        result = True
        return 
    for i in li[x]:
        if not check[i]:
            check[i] = True
            dfs(i, y + 1)
            check[i] = False
# 방문을 확인하는 dfs를 만들고 깊이를 확인할 변수를 같이 입력하여 깊이가 충분하면 
# result 값을 True로 변환하여 출력해줍니다.
for i in range(n):
    # 모든 변수에서 출발하여 
    dfs(i, 0)
    check[i] = False
    if result:
        break
    # result 값이 True로 반환되었다면 조건의 관계를 충족하므로 반복을 그만해도 됩니다.
if result:
    print(1)
    # result값이 True라면 1을
else:
    print(0)
    # 아니면 0을 출력합니다.

# 체크를 불리언이 아닌 정수로하여 기본을 0으로 시작하였다가 출발 자리까지 한 바퀴 돌아 관계가 적용되는 경우가 생겨서 오답이 나왔었다.
# 이런 상황이 반복될 수 있으니 이런 문제의 경우에는 불리언을 쓰는 습관을 들일 필요가 있을것같다.