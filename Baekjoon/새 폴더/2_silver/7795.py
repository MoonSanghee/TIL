tc = int(input())
for t in range(tc):
    a, b = map(int, input().split())
    alist = list(map(int, input().split()))
    blist = list(map(int, input().split()))
    alist.sort()
    blist.sort()

    result = 0
    cnt = 0
    for i in range(a):
        while True:
            if cnt == b or alist[i] <= blist[cnt]:
                result += cnt
                break
            else:
                cnt += 1
    print(result)