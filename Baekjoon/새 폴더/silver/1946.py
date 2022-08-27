t = int(input().strip())
for i in range(t):
    n = int(input())
    ranks = []
    for j in range(n):
        rank = list(map(int, input().split()))
        ranks.append(rank)

    ranks.sort()
    bench = ranks[0][1]
    cnt = 1

    for j in range(n):
        if bench > ranks[j][1]:
            cnt += 1
            bench = ranks[j][1]
    print(cnt)
# print(ranks)