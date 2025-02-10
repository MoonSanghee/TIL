n = int(input())

for i in range(100000000):
    i = str(i)
    if len(i) <= n:
        n -= len(i)
    else:
        print(i[n])
        break