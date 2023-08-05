li = [int(input()) for _ in range(8)]
s = sorted(li)

r = 0
for i in range(3, 8):
    r += s[i]
print(r)
p = []
for i in range(3, 8):
    p.append(li.index(s[i]) + 1)
p.sort()
print(*p)