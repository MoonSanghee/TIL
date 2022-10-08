n, m = map(int, input().split())
li = []

def make(x, y):
    if y == m:
        return print(*li)
    for i in range(x, n + 1):
        li.append(i)
        make(i, y + 1)
        li.pop()

for i in range(1, n + 1):
    li.append(i)
    make(i, 1)
    li.pop()