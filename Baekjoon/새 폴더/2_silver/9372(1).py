import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    for _ in range(m):
        a, b = map(int,input().split())
    print(n - 1)
    # 모든 국가가 연결되어 있으니 출발지를 제외한 모든 국가를 방문하면 되기에 n -1종류의 비행을 하면 된다.

