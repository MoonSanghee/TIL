x = []
y = []
for i in range(3):
    a,b = map(int, input().split())
    if a not in x:
        x.append(a)
    else:
        x.remove(a)
    if b not in y:
        y.append(b)
    else:
        y.remove(b)
print(x[0], y[0])