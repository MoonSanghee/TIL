n,m = map(int, input().split())
nums = [i for i in range(1, n + 1)]
li = []
def make(x):
    if x == m:
        return print(*li)
    for i in range(1, n + 1):
        li.append(i)
        make(x + 1)
        li.pop()
make(0)