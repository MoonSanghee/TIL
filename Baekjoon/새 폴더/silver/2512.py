n = int(input())
wants = list(map(int, input().split()))
limit = int(input())
s, e = 1, max(wants)
while s <= e:
    mid = (s+e)//2
    cnt = 0
    for i in wants:
        if i < mid:
            cnt += i
        else:
            cnt += mid
    if cnt > limit:
        e = mid - 1
    else:
        s = mid + 1
print(e)