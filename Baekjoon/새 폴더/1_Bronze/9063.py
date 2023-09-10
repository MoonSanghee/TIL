xlist = []
ylist = []
for _ in range(int(input())) :
    x, y = map(int, input().split())
    xlist.append(x)
    ylist.append(y)
print((max(xlist) - min(xlist)) * (max(ylist) - min(ylist)))