T = int(input())

def check(i):
    global cnt
    if i <= n:
        check(2 * i)
        tree[i] = cnt
        cnt += 1
        check(2 * i + 1)


for tc in range(1, T + 1):
    n = int(input())
    tree = [0 for _ in range(n + 1)]

    cnt = 1
    check(1)
    print(f"#{tc} {tree[1]} {tree[n//2]}")