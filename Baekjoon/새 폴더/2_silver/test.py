n = int(input())
wine = []
for i in range(n):
    wine.append(int(input()))
w1 = [0, 0]
w2 = [0, wine[0]]
for i in range(1, n):
    w1.append(w2[i - 1] + wine[i])
    w2.append(max(max(w1[i - 2], w2[i - 2]) + wine[i]), w1[i - 1], w2[i - 2])
