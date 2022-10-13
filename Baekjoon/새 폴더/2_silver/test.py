a = []
for i in range(10):
    a.append(list(map(int, input().split())))
a.sort(key=lambda x:x[0] + x[1])
print(a)