n, m = map(int, input().split())

card = []
cnt = 0

for _ in range(m):
    a, b = map(int, input().split())

    if a < n:
        card.append((a, b))
    else:
        cnt += 1

card.sort(reverse = True)

result = 0

if m - 1 == cnt:
    print(0)
else:
    for i in range(m - 1- cnt):
        result += n - card[i][0]
    print(result)