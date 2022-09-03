n, m = map(int, input().split())
tree = list(map(int, input().split()))

s, e = 1, max(tree)

while s <= e:
    mid = (s+e)//2
    cnt = 0
    for i in tree:
        if i > mid:
            cnt += i - mid
    if cnt >= m:
        s = mid + 1
    else:
        e = mid - 1
print(e)