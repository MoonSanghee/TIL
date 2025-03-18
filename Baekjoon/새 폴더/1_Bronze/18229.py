n, m, k = map(int, input().split())
distance = [0] * n
moves = [list(map(int, input().split())) for _ in range(n)]
flag = False

for i in range(m):
    if not flag:
        for j in range(n):
            distance[j] += moves[j][i]
            if distance[j] >= k:
                print(j + 1, i + 1)
                flag = True
                break