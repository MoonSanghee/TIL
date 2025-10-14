c = []
d = []

for i in range(3):
    a, b = map(int, input().split())
    c.append(a)
    d.append(b)

energy = int(input())
result = 0
energy -= sum(d)

while True:
    if energy <= 0:
        print(result)
        break
    result += 1
    for i in range(3):
        if result % c[i] == 0:
            energy -= d[i]