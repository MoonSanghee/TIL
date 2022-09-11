n = int(input())
d = [0]
for i in range(n):
    d.append(int(input()))

d1 = [0, 0]
d2 = [0, d[1]]
for i in range(2, n + 1):
    d1.append(d2[i - 1] + d[i])
    d2.append(max(d1[i - 2], d2[i - 2]) + d[i])
print(max(d1[n], d2[n]))