# 나의 풀이
n = int(input())
wine = []
for i in range(n):
    wine.append(int(input()))
w1 = [0, 0]
w2 = [0, wine[0]]
for i in range(1, n):
    w1.append(w2[i] + wine[i])
    w2.append(max(max(w1[i - 1], w2[i - 1]) + wine[i], w1[i], w2[i]))
print(max(w1[-1], w2[-1]))

# 찾아본 풀이
n = int(input())
wine = []
for _ in range(n):
    wine.append(int(input()))

d = [0 for _ in range(n)]

d[0] == wine[0]

if n > 1:
    d[1] = wine[0] + wine[1]

if n > 2:
    d[2] = max(wine[2] + wine[1], wine[2] + wine[0], d[1])