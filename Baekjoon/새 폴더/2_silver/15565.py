n, k =map(int, input().split())
li = list(map(int, input().split()))
s, e = 0, 0
cnt = 0
result = 1000001

for start in range(n):
    while cnt < k and e < n:
        s += 1
        if li[e] == 1:
            cnt += 1
        e += 1

    if cnt == k and result > s:
        result = s

    if li[start] == 1:
        cnt -= 1
    s -= 1

if result != 1000001:
    print(result)
else:
    print(-1)